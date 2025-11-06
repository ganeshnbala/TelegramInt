# install_dependencies.py
# Script to install required dependencies for Telegram bot

import subprocess
import sys

def install_dependencies():
    """Install required dependencies for Telegram bot."""
    
    dependencies = [
        "python-telegram-bot>=21.0.0",
        "openpyxl>=3.1.0",
        "pandas>=2.0.0",
        "python-dotenv>=1.0.0",
    ]
    
    print("=" * 60)
    print("Installing Telegram Bot Dependencies")
    print("=" * 60)
    print()
    
    for dep in dependencies:
        print(f"Installing {dep}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✅ {dep} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {dep}: {e}")
            return False
        print()
    
    print("=" * 60)
    print("✅ All dependencies installed successfully!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Run: python setup_telegram.py")
    print("2. Run: python test_telegram_bot.py (to verify setup)")
    print("3. Run: python telegram_bot.py (to start the bot)")
    print()
    
    return True


if __name__ == "__main__":
    install_dependencies()

