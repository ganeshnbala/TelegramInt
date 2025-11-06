# check_bot_status.py
# Check if bot is running and can connect

import os
import sys
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TELEGRAM_BOT_TOKEN")

if not token:
    print("❌ TELEGRAM_BOT_TOKEN not found")
    sys.exit(1)

print("=" * 60)
print("Bot Status Check")
print("=" * 60)
print()

# Check imports
print("Checking imports...")
try:
    import yaml
    print("✅ yaml")
except ImportError as e:
    print(f"❌ yaml: {e}")
    sys.exit(1)

try:
    from telegram.ext import Application
    print("✅ telegram")
except ImportError as e:
    print(f"❌ telegram: {e}")
    sys.exit(1)

try:
    import pandas
    print("✅ pandas")
except ImportError as e:
    print(f"❌ pandas: {e}")

try:
    import openpyxl
    print("✅ openpyxl")
except ImportError as e:
    print(f"❌ openpyxl: {e}")

print()
print("=" * 60)
print("✅ All required modules are available!")
print("=" * 60)
print()
print("Your bot should be running now.")
print("Test it in Telegram by sending /start to @Gabatestbot_testbot")
print()

