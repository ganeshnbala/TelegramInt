# add_token.py
# Quick script to add Telegram token to .env file

import os
from pathlib import Path

def add_telegram_token(token: str):
    """Add or update Telegram token in .env file."""
    
    env_file = Path(".env")
    
    # If .env doesn't exist, create it with token
    if not env_file.exists():
        print("Creating new .env file...")
        env_content = f"""# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN={token}

# Gmail Configuration
# Note: Use an App Password, not your regular Gmail password
# To create an App Password: https://support.google.com/accounts/answer/185833
GMAIL_SENDER=
GMAIL_PASSWORD=
GMAIL_RECIPIENT=

# Excel Export Configuration
EXCEL_FILE_PATH=exports/agent_results.xlsx
USE_APPEND_MODE=true
"""
        env_file.write_text(env_content)
        print(f"✅ Created .env file with Telegram token")
        print(f"⚠️  Don't forget to add Gmail credentials!")
        return True
    
    # If .env exists, update the token
    lines = env_file.read_text().splitlines()
    updated = False
    new_lines = []
    
    for line in lines:
        if line.startswith("TELEGRAM_BOT_TOKEN="):
            new_lines.append(f"TELEGRAM_BOT_TOKEN={token}")
            updated = True
            print("✅ Updated existing Telegram token")
        else:
            new_lines.append(line)
    
    if not updated:
        # Token line doesn't exist, add it at the top
        new_lines.insert(0, f"TELEGRAM_BOT_TOKEN={token}")
        print("✅ Added Telegram token to .env file")
    
    env_file.write_text("\n".join(new_lines))
    return True


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        token = sys.argv[1]
    else:
        print("=" * 60)
        print("Add Telegram Bot Token")
        print("=" * 60)
        print()
        token = input("Enter your Telegram Bot Token: ").strip()
    
    if not token:
        print("❌ Token cannot be empty!")
        sys.exit(1)
    
    if add_telegram_token(token):
        print()
        print("✅ Token added successfully!")
        print()
        print("Next steps:")
        print("1. Add Gmail credentials (run: python setup_telegram.py)")
        print("2. Test configuration (run: python test_telegram_bot.py)")
        print("3. Start bot (run: python telegram_bot.py)")

