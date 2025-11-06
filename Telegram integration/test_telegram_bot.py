# test_telegram_bot.py
# Test script to verify Telegram bot configuration

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def test_configuration():
    """Test if all required configuration is present."""
    
    print("=" * 60)
    print("Testing Telegram Bot Configuration")
    print("=" * 60)
    print()
    
    # Load .env file
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found!")
        print("   Run: python setup_telegram.py")
        return False
    
    load_dotenv()
    
    # Check required variables
    required_vars = {
        "TELEGRAM_BOT_TOKEN": "Telegram Bot Token",
        "GMAIL_SENDER": "Gmail Sender Address",
        "GMAIL_PASSWORD": "Gmail App Password",
        "GMAIL_RECIPIENT": "Gmail Recipient Address",
    }
    
    missing_vars = []
    for var, name in required_vars.items():
        value = os.getenv(var)
        if not value:
            missing_vars.append(name)
            print(f"❌ {name}: Not set")
        else:
            # Mask sensitive values
            if "PASSWORD" in var or "TOKEN" in var:
                masked = value[:4] + "*" * (len(value) - 8) + value[-4:] if len(value) > 8 else "****"
                print(f"✅ {name}: {masked}")
            else:
                print(f"✅ {name}: {value}")
    
    print()
    
    if missing_vars:
        print("❌ Missing required configuration:")
        for var in missing_vars:
            print(f"   - {var}")
        print()
        print("Run: python setup_telegram.py")
        return False
    
    # Check dependencies
    print("Checking dependencies...")
    print()
    
    dependencies = [
        ("telegram", "python-telegram-bot"),
        ("pandas", "pandas"),
        ("openpyxl", "openpyxl"),
        ("dotenv", "python-dotenv"),
    ]
    
    missing_deps = []
    for module, package in dependencies:
        try:
            if module == "dotenv":
                __import__("dotenv")
            elif module == "telegram":
                __import__("telegram")
            else:
                __import__(module)
            print(f"✅ {package}: Installed")
        except ImportError:
            missing_deps.append(package)
            print(f"❌ {package}: Not installed")
    
    print()
    
    if missing_deps:
        print("❌ Missing dependencies:")
        for dep in missing_deps:
            print(f"   - {dep}")
        print()
        print("Install with: pip install " + " ".join(missing_deps))
        return False
    
    # Check if exports directory can be created
    excel_path = os.getenv("EXCEL_FILE_PATH", "exports/agent_results.xlsx")
    excel_dir = os.path.dirname(excel_path)
    
    if excel_dir:
        try:
            Path(excel_dir).mkdir(parents=True, exist_ok=True)
            print(f"✅ Excel directory: {excel_dir} (ready)")
        except Exception as e:
            print(f"❌ Cannot create Excel directory: {e}")
            return False
    
    print()
    print("=" * 60)
    print("✅ All checks passed! Configuration is ready.")
    print("=" * 60)
    print()
    print("You can now run: python telegram_bot.py")
    print()
    
    return True


if __name__ == "__main__":
    success = test_configuration()
    sys.exit(0 if success else 1)

