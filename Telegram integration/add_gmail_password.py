# add_gmail_password.py
# Quick script to add Gmail App Password to .env file

import os
from pathlib import Path

def add_gmail_password(password: str):
    """Add or update Gmail password in .env file."""
    
    env_file = Path(".env")
    
    if not env_file.exists():
        print("❌ .env file not found!")
        print("   Run: python setup_telegram.py first")
        return False
    
    # Read current content
    lines = env_file.read_text().splitlines()
    updated = False
    new_lines = []
    
    for line in lines:
        if line.startswith("GMAIL_PASSWORD="):
            new_lines.append(f"GMAIL_PASSWORD={password}")
            updated = True
        else:
            new_lines.append(line)
    
    if not updated:
        print("❌ GMAIL_PASSWORD line not found in .env file")
        return False
    
    # Write back
    env_file.write_text("\n".join(new_lines))
    print("✅ Gmail password added successfully!")
    return True


if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("Add Gmail App Password")
    print("=" * 60)
    print()
    print("📋 Steps to get App Password:")
    print("1. Go to: https://myaccount.google.com/apppasswords")
    print("2. Select 'Mail' → 'Other (Custom name)' → Type 'Agent Bot'")
    print("3. Click 'Generate' and copy the 16-character password")
    print()
    
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter your Gmail App Password (16 characters, no spaces): ").strip()
    
    if not password:
        print("❌ Password cannot be empty!")
        sys.exit(1)
    
    # Remove spaces if user included them
    password = password.replace(" ", "")
    
    if len(password) != 16:
        print(f"⚠️  Warning: Password should be 16 characters (you entered {len(password)})")
        confirm = input("Continue anyway? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            sys.exit(1)
    
    if add_gmail_password(password):
        print()
        print("✅ Configuration complete!")
        print()
        print("Next steps:")
        print("1. Test: python test_telegram_bot.py")
        print("2. Start bot: python telegram_bot.py")
        print()

