@echo off
echo ========================================
echo Starting Telegram Bot
echo ========================================
echo.

cd /d "%~dp0"

REM Check if .env exists
if not exist .env (
    echo .env file not found!
    echo Please run: py setup_telegram.py
    pause
    exit /b 1
)

echo Starting bot...
echo Press Ctrl+C to stop
echo.

py telegram_bot.py

pause

