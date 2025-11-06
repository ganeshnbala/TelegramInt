# telegram_bot.py

import asyncio
import yaml
import os
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from core.loop import AgentLoop
from core.session import MultiMCP
from modules.excel_export import create_excel_from_result, append_to_excel
from modules.gmail_sender import send_excel_to_gmail

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GMAIL_RECIPIENT = os.getenv("GMAIL_RECIPIENT")
EXCEL_FILE_PATH = os.getenv("EXCEL_FILE_PATH", "exports/agent_results.xlsx")
USE_APPEND_MODE = os.getenv("USE_APPEND_MODE", "true").lower() == "true"


async def process_message_with_agent(user_input: str) -> str:
    """
    Process a user message through the agent and return the result.
    
    Args:
        user_input: The message from Telegram
        
    Returns:
        The agent's final answer
    """
    try:
        # Load MCP server configs from profiles.yaml
        # Try multiple possible paths
        possible_paths = [
            Path("config/profiles.yaml"),
            Path("S8 Share/config/profiles.yaml"),
            Path(__file__).parent.parent / "config" / "profiles.yaml",
            Path(__file__).parent / "config" / "profiles.yaml",
        ]
        
        config_path = None
        for path in possible_paths:
            if path.exists():
                config_path = path
                break
        
        if not config_path:
            raise FileNotFoundError("Could not find config/profiles.yaml in any expected location")
        
        with open(config_path, "r") as f:
            profile = yaml.safe_load(f)
            mcp_servers = profile.get("mcp_servers", [])
        
        # Initialize MCP
        multi_mcp = MultiMCP(server_configs=mcp_servers)
        await multi_mcp.initialize()
        
        # Create and run agent
        agent = AgentLoop(
            user_input=user_input,
            dispatcher=multi_mcp
        )
        
        final_response = await agent.run()
        
        # Clean up the response
        if final_response.startswith("FINAL_ANSWER:"):
            final_response = final_response.replace("FINAL_ANSWER:", "").strip()
        
        return final_response
        
    except Exception as e:
        logger.error(f"Agent processing failed: {e}")
        return f"Error processing your request: {str(e)}"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming Telegram messages."""
    user_message = update.message.text
    user_id = update.effective_user.id
    username = update.effective_user.username or "Unknown"
    
    logger.info(f"Received message from {username} ({user_id}): {user_message}")
    
    # Send "processing" message
    processing_msg = await update.message.reply_text("🤔 Processing your request...")
    
    try:
        # Process message through agent
        agent_response = await process_message_with_agent(user_message)
        
        # Send result immediately (don't wait for Excel/email)
        await processing_msg.edit_text(f"✅ Result:\n\n{agent_response}")
        
        # Prepare metadata
        metadata = {
            "User ID": user_id,
            "Username": username,
            "Chat ID": update.effective_chat.id
        }
        
        # Export to Excel and send email in background (non-blocking)
        async def save_and_email():
            try:
                if USE_APPEND_MODE:
                    excel_path = append_to_excel(
                        user_message=user_message,
                        agent_response=agent_response,
                        excel_path=EXCEL_FILE_PATH,
                        metadata=metadata
                    )
                else:
                    excel_path = create_excel_from_result(
                        user_message=user_message,
                        agent_response=agent_response,
                        metadata=metadata
                    )
                
                logger.info(f"Excel file created/updated: {excel_path}")
                
                # Send to Gmail (non-blocking)
                if GMAIL_RECIPIENT:
                    # Run email sending in executor to avoid blocking
                    loop = asyncio.get_event_loop()
                    success = await loop.run_in_executor(
                        None,
                        send_excel_to_gmail,
                        excel_path,
                        GMAIL_RECIPIENT
                    )
                    
                    if success:
                        await update.message.reply_text(
                            f"📧 Results have been sent to {GMAIL_RECIPIENT}"
                        )
                        logger.info(f"Email sent successfully to {GMAIL_RECIPIENT}")
                    else:
                        await update.message.reply_text(
                            "⚠️ Results saved, but email sending failed. Check logs."
                        )
                        logger.error("Failed to send email")
                else:
                    logger.warning("GMAIL_RECIPIENT not set, skipping email send")
                    
            except Exception as e:
                logger.error(f"Failed to export to Excel or send email: {e}", exc_info=True)
                try:
                    await update.message.reply_text(
                        f"⚠️ Result saved, but email failed: {str(e)}"
                    )
                except:
                    pass
        
        # Start background task (don't await - let it run in background)
        asyncio.create_task(save_and_email())
            
    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await processing_msg.edit_text(f"❌ Error: {str(e)}")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    welcome_message = """
🤖 Welcome to the Agent Bot!

Send me a message and I'll:
1. Process it through the AI agent
2. Save the results to an Excel file
3. Email the results to the configured Gmail account

Just send me your question or request!
"""
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command."""
    help_text = """
📖 Available Commands:

/start - Start the bot and see welcome message
/help - Show this help message
/status - Check bot status

Just send a message to get it processed by the agent!
"""
    await update.message.reply_text(help_text)


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /status command."""
    status_info = f"""
📊 Bot Status:

✅ Bot is running
📧 Email recipient: {GMAIL_RECIPIENT or "Not configured"}
📁 Excel file: {EXCEL_FILE_PATH}
🔄 Append mode: {"Enabled" if USE_APPEND_MODE else "Disabled"}
"""
    await update.message.reply_text(status_info)


def main():
    """Start the Telegram bot."""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not set in environment variables!")
        raise ValueError("TELEGRAM_BOT_TOKEN is required")
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    logger.info("Starting Telegram bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

