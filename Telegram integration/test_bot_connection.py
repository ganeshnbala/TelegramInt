# test_bot_connection.py
# Quick test to verify bot can connect to Telegram

import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

token = os.getenv("TELEGRAM_BOT_TOKEN")

if not token:
    print("❌ TELEGRAM_BOT_TOKEN not found in .env")
    exit(1)

print("Testing Telegram bot connection...")
print(f"Token: {token[:10]}...")

try:
    import asyncio
    bot = Bot(token=token)
    
    async def test_connection():
        bot_info = await bot.get_me()
        print(f"\n✅ Bot connected successfully!")
        print(f"Bot name: {bot_info.first_name}")
        print(f"Bot username: @{bot_info.username}")
        print(f"Bot ID: {bot_info.id}")
        print("\n✅ Your bot is ready to receive messages!")
    
    asyncio.run(test_connection())
except Exception as e:
    print(f"\n❌ Error connecting to Telegram: {e}")
    print("\nPossible issues:")
    print("1. Invalid bot token")
    print("2. No internet connection")
    print("3. Telegram API is down")

