# send_latest_results.py
# Manually send the latest Excel results via email

import os
import glob
from dotenv import load_dotenv
from modules.gmail_sender import send_excel_to_gmail

load_dotenv()

print("=" * 60)
print("Send Latest Results via Email")
print("=" * 60)
print()

# Find latest Excel file
excel_files = glob.glob("exports/*.xlsx")
if not excel_files:
    print("❌ No Excel files found in exports folder")
    exit(1)

# Get the most recent file
latest_file = max(excel_files, key=lambda x: os.path.getmtime(x))
print(f"📄 Latest Excel file: {latest_file}")
print(f"   Modified: {os.path.getmtime(latest_file)}")
print()

# Check if agent_results.xlsx exists (append mode)
if os.path.exists("exports/agent_results.xlsx"):
    file_to_send = "exports/agent_results.xlsx"
    print(f"📊 Using append mode file: {file_to_send}")
else:
    file_to_send = latest_file
    print(f"📊 Using latest file: {file_to_send}")

print()

# Send email
recipient = os.getenv("GMAIL_RECIPIENT")
if not recipient:
    print("❌ GMAIL_RECIPIENT not set in .env")
    exit(1)

print(f"📧 Sending to: {recipient}")
print()

try:
    success = send_excel_to_gmail(
        excel_path=file_to_send,
        recipient_email=recipient,
        subject="Your Agent Results - Latest Data"
    )
    
    if success:
        print("✅ Email sent successfully!")
        print(f"📬 Check your inbox at: {recipient}")
        print("   (Also check Spam/Junk folder)")
    else:
        print("❌ Email sending failed")
        print("   Check the error messages above")
except Exception as e:
    print(f"❌ Error: {e}")

print()
print("=" * 60)

