# setup_telegram.py
# Interactive setup script for Telegram bot configuration

import os
from pathlib import Path

def create_env_file():
    """Interactive script to create .env file with Telegram and Gmail credentials."""
    
    print("=" * 60)
    print("Telegram Bot Setup")
    print("=" * 60)
    print()
    
    print("STEP 1: Telegram Bot Token")
    print("-" * 60)
    print("1. Open Telegram and search for @BotFather")
    print("2. Send /newbot command")
    print("3. Follow the prompts to create your bot")
    print("4. Copy the token you receive")
    print()
    
    telegram_token = input("Enter your Telegram Bot Token: ").strip()
    if not telegram_token:
        print("❌ Telegram token is required!")
        return False
    
    print()
    print("STEP 2: Gmail Configuration")
    print("-" * 60)
    print("1. Go to: https://myaccount.google.com/apppasswords")
    print("2. Create an App Password for 'Mail'")
    print("3. Copy the 16-character password (remove spaces)")
    print()
    
    gmail_sender = input("Enter your Gmail address: ").strip()
    if not gmail_sender:
        print("❌ Gmail address is required!")
        return False
    
    gmail_password = input("Enter your Gmail App Password (16 characters, no spaces): ").strip()
    if not gmail_password:
        print("❌ Gmail password is required!")
        return False
    
    gmail_recipient = input("Enter recipient email (where to send Excel files): ").strip()
    if not gmail_recipient:
        print("⚠️  No recipient specified. You can set this later in .env file.")
        gmail_recipient = gmail_sender  # Default to sender
    
    print()
    print("STEP 3: Excel Configuration")
    print("-" * 60)
    excel_path = input("Enter Excel file path (press Enter for default: exports/agent_results.xlsx): ").strip()
    if not excel_path:
        excel_path = "exports/agent_results.xlsx"
    
    use_append = input("Append all results to one file? (y/n, default: y): ").strip().lower()
    use_append_mode = "true" if use_append != "n" else "false"
    
    # Create .env file content
    env_content = f"""# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN={telegram_token}

# Gmail Configuration
# Note: Use an App Password, not your regular Gmail password
# To create an App Password: https://support.google.com/accounts/answer/185833
GMAIL_SENDER={gmail_sender}
GMAIL_PASSWORD={gmail_password}
GMAIL_RECIPIENT={gmail_recipient}

# Excel Export Configuration
EXCEL_FILE_PATH={excel_path}
USE_APPEND_MODE={use_append_mode}
"""
    
    # Write .env file
    env_file = Path(".env")
    if env_file.exists():
        overwrite = input(f"\n.env file already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != "y":
            print("❌ Setup cancelled.")
            return False
    
    try:
        env_file.write_text(env_content)
        print()
        print("=" * 60)
        print("✅ .env file created successfully!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. Install dependencies: pip install python-telegram-bot openpyxl pandas python-dotenv")
        print("2. Run the bot: python telegram_bot.py")
        print("3. Find your bot on Telegram and send /start")
        print()
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False


if __name__ == "__main__":
    create_env_file()

