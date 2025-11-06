@echo off
echo ========================================
echo Starting Telegram Bot
echo ========================================
echo.

REM Check if .env exists
if not exist .env (
    echo .env file not found!
    echo.
    echo Running setup script...
    python setup_telegram.py
    echo.
    if not exist .env (
        echo Setup failed. Please run setup_telegram.py manually.
        pause
        exit /b 1
    )
)

REM Check dependencies
echo Checking dependencies...
python test_telegram_bot.py
if errorlevel 1 (
    echo.
    echo Installing missing dependencies...
    python install_dependencies.py
    echo.
)

echo.
echo Starting bot...
echo Press Ctrl+C to stop
echo.
python telegram_bot.py

pause

