# test_full_workflow.py
# Test the complete workflow: Agent -> Excel -> Email

import asyncio
import yaml
from pathlib import Path
from dotenv import load_dotenv
import os

from core.loop import AgentLoop
from core.session import MultiMCP
from modules.excel_export import create_excel_from_result
from modules.gmail_sender import send_excel_to_gmail

load_dotenv()

async def test_agent_and_email():
    """Test the full workflow: process message through agent, save to Excel, send email."""
    
    print("=" * 60)
    print("Testing Full Workflow: Agent -> Excel -> Email")
    print("=" * 60)
    print()
    
    # Test message
    user_message = "What are the top 10 biggest cities in the world?"
    print(f"📝 User Message: {user_message}")
    print()
    
    # Step 1: Process through agent
    print("Step 1: Processing through AI Agent...")
    print("-" * 60)
    
    try:
        # Load MCP server configs
        config_path = Path("config/profiles.yaml")
        if not config_path.exists():
            config_path = Path("S8 Share/config/profiles.yaml")
        
        with open(config_path, "r") as f:
            profile = yaml.safe_load(f)
            mcp_servers = profile.get("mcp_servers", [])
        
        # Initialize MCP
        multi_mcp = MultiMCP(server_configs=mcp_servers)
        await multi_mcp.initialize()
        
        # Create and run agent
        agent = AgentLoop(
            user_input=user_message,
            dispatcher=multi_mcp
        )
        
        final_response = await agent.run()
        
        # Clean up the response
        if final_response.startswith("FINAL_ANSWER:"):
            final_response = final_response.replace("FINAL_ANSWER:", "").strip()
        
        print(f"✅ Agent Response:\n{final_response}\n")
        
    except Exception as e:
        print(f"❌ Agent processing failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Step 2: Create Excel file
    print("Step 2: Creating Excel file...")
    print("-" * 60)
    
    try:
        excel_path = create_excel_from_result(
            user_message=user_message,
            agent_response=final_response,
            metadata={
                "Test": "Full Workflow Test",
                "Source": "Manual Test Script"
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
            subject="Test: Top 10 Biggest Cities in the World - Agent Results",
            body=f"""Hello,

This is a test email from the Agent workflow.

Question: {user_message}

Agent Response:
{final_response}

The full results are attached in the Excel file.

Best regards,
Agent Bot Test Script
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
    print("✅ Full workflow test completed successfully!")
    print("=" * 60)
    print()
    print("Summary:")
    print(f"  ✅ Agent processed: {user_message}")
    print(f"  ✅ Excel created: {excel_path}")
    print(f"  ✅ Email sent to: {recipient}")
    print()
    
    return True


if __name__ == "__main__":
    result = asyncio.run(test_agent_and_email())
    exit(0 if result else 1)

