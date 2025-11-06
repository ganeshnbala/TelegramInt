# modules/gmail_sender.py

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from typing import Optional, List
import logging

logger = logging.getLogger(__name__)


def send_email_with_attachment(
    sender_email: str,
    sender_password: str,
    recipient_email: str,
    subject: str,
    body: str,
    attachment_path: str,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587
) -> bool:
    """
    Send an email with an Excel attachment via Gmail SMTP.
    
    Args:
        sender_email: Gmail address of the sender
        sender_password: Gmail app password (not regular password)
        recipient_email: Email address of the recipient
        subject: Email subject
        body: Email body text
        attachment_path: Path to the Excel file to attach
        smtp_server: SMTP server (default: Gmail)
        smtp_port: SMTP port (default: 587 for TLS)
        
    Returns:
        True if email sent successfully, False otherwise
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Add body
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach file
        if os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            
            filename = os.path.basename(attachment_path)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {filename}'
            )
            
            msg.attach(part)
        else:
            logger.warning(f"Attachment file not found: {attachment_path}")
            return False
        
        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, sender_password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        logger.info(f"Email sent successfully to {recipient_email}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return False


def send_excel_to_gmail(
    excel_path: str,
    recipient_email: str,
    sender_email: Optional[str] = None,
    sender_password: Optional[str] = None,
    subject: Optional[str] = None,
    body: Optional[str] = None
) -> bool:
    """
    Convenience function to send Excel file to Gmail using environment variables.
    
    Args:
        excel_path: Path to the Excel file
        recipient_email: Email address of the recipient
        sender_email: Gmail address (if None, uses GMAIL_SENDER from env)
        sender_password: Gmail app password (if None, uses GMAIL_PASSWORD from env)
        subject: Email subject (if None, uses default)
        body: Email body (if None, uses default)
        
    Returns:
        True if email sent successfully, False otherwise
    """
    # Get credentials from environment if not provided
    sender_email = sender_email or os.getenv("GMAIL_SENDER")
    sender_password = sender_password or os.getenv("GMAIL_PASSWORD")
    
    if not sender_email or not sender_password:
        logger.error("Gmail credentials not provided. Set GMAIL_SENDER and GMAIL_PASSWORD environment variables.")
        return False
    
    # Default subject and body
    if not subject:
        filename = os.path.basename(excel_path)
        subject = f"Agent Results - {filename}"
    
    if not body:
        body = f"""Hello,

Please find attached the agent results in Excel format.

File: {os.path.basename(excel_path)}

Best regards,
Agent Bot
"""
    
    return send_email_with_attachment(
        sender_email=sender_email,
        sender_password=sender_password,
        recipient_email=recipient_email,
        subject=subject,
        body=body,
        attachment_path=excel_path
    )

