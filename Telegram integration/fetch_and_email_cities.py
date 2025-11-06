# fetch_and_email_cities.py
# Fetch top 10 cities online, process through agent, and email results

import asyncio
import yaml
from pathlib import Path
from dotenv import load_dotenv
import os
import sys

from core.loop import AgentLoop
from core.session import MultiMCP
from modules.excel_export import create_excel_from_result
from modules.gmail_sender import send_excel_to_gmail

load_dotenv()

async def fetch_cities_and_email():
    """Fetch top 10 cities online, process through agent, and email results."""
    
    print("=" * 60)
    print("Fetch Top 10 Cities Online → Agent → Email")
    print("=" * 60)
    print()
    
    # Query that will trigger web search
    user_message = "What are the top 10 biggest cities in the world by population? Search online and provide the list with their populations."
    print(f"📝 Query: {user_message}")
    print()
    
    # Step 1: Process through agent (which will use web search)
    print("Step 1: Processing through AI Agent with Web Search...")
    print("-" * 60)
    
    try:
        # Load MCP server configs
        config_path = Path("config/profiles.yaml")
        if not config_path.exists():
            config_path = Path("S8 Share/config/profiles.yaml")
        
        with open(config_path, "r") as f:
            profile = yaml.safe_load(f)
            mcp_servers = profile.get("mcp_servers", [])
        
        # Fix paths to be relative to current directory
        current_dir = Path.cwd()
        for server in mcp_servers:
            if server.get("cwd") == ".":
                server["cwd"] = str(current_dir)
            # Make script path absolute if needed
            script_path = Path(server["script"])
            if not script_path.is_absolute():
                server["script"] = str(current_dir / script_path)
        
        print(f"Initializing MCP servers from: {current_dir}")
        
        # Initialize MCP
        multi_mcp = MultiMCP(server_configs=mcp_servers)
        await multi_mcp.initialize()
        
        print("✅ MCP servers initialized")
        print(f"Available tools: {await multi_mcp.list_all_tools()}")
        print()
        
        # Create and run agent
        print("Running agent...")
        agent = AgentLoop(
            user_input=user_message,
            dispatcher=multi_mcp
        )
        
        final_response = await agent.run()
        
        # Clean up the response
        if final_response.startswith("FINAL_ANSWER:"):
            final_response = final_response.replace("FINAL_ANSWER:", "").strip()
        
        print(f"✅ Agent Response:\n{final_response}\n")
        
        if "[no result]" in final_response.lower() or not final_response.strip():
            print("⚠️ Warning: Agent didn't return a proper result")
            print("This might be due to missing API keys or MCP server issues")
        
    except Exception as e:
        print(f"❌ Agent processing failed: {e}")
        import traceback
        traceback.print_exc()
        # Still create Excel and send email with error message
        final_response = f"Error processing request: {str(e)}"
    
    # Step 2: Create Excel file
    print("Step 2: Creating Excel file...")
    print("-" * 60)
    
    try:
        excel_path = create_excel_from_result(
            user_message=user_message,
            agent_response=final_response,
            metadata={
                "Source": "Web Search + Agent",
                "Query Type": "Top 10 Cities"
            }
        )
        print(f"✅ Excel file created: {excel_path}\n")
    except Exception as e:
        print(f"❌ Excel creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Step 3: Send email
    print("Step 3: Sending email...")
    print("-" * 60)
    
    try:
        recipient = os.getenv("GMAIL_RECIPIENT")
        if not recipient:
            print("❌ GMAIL_RECIPIENT not set in .env")
            return False
        
        success = send_excel_to_gmail(
            excel_path=excel_path,
            recipient_email=recipient,
            subject="Top 10 Biggest Cities in the World - Agent Results",
            body=f"""Hello,

Here are the results from the agent's web search for the top 10 biggest cities in the world.

Query: {user_message}

Agent Response:
{final_response}

The full results are attached in the Excel file.

Best regards,
Agent Bot
"""
        )
        
        if success:
            print(f"✅ Email sent successfully to {recipient}!")
            print("📬 Check your inbox (and spam folder)")
        else:
            print("❌ Email sending failed")
            return False
            
    except Exception as e:
        print(f"❌ Email sending failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print()
    print("=" * 60)
    print("✅ Complete workflow finished!")
    print("=" * 60)
    print()
    print("Summary:")
    print(f"  ✅ Query processed: {user_message}")
    print(f"  ✅ Excel created: {excel_path}")
    print(f"  ✅ Email sent to: {recipient}")
    print()
    
    return True


if __name__ == "__main__":
    result = asyncio.run(fetch_cities_and_email())
    sys.exit(0 if result else 1)

