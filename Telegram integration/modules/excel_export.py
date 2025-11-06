# modules/excel_export.py

import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import os


def create_excel_from_result(
    user_message: str,
    agent_response: str,
    metadata: Optional[Dict[str, Any]] = None,
    output_dir: str = "exports"
) -> str:
    """
    Create an Excel file with the user message and agent response.
    
    Args:
        user_message: The original message from Telegram
        agent_response: The final answer from the agent
        metadata: Optional metadata (timestamp, user_id, etc.)
        output_dir: Directory to save the Excel file
        
    Returns:
        Path to the created Excel file
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Prepare data
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data = {
        "Timestamp": [timestamp],
        "User Message": [user_message],
        "Agent Response": [agent_response],
    }
    
    # Add metadata if provided
    if metadata:
        for key, value in metadata.items():
            data[key] = [value]
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Generate filename with timestamp
    filename = f"agent_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join(output_dir, filename)
    
    # Write to Excel
    df.to_excel(filepath, index=False, engine='openpyxl')
    
    return filepath


def append_to_excel(
    user_message: str,
    agent_response: str,
    excel_path: str,
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Append a new row to an existing Excel file or create a new one.
    
    Args:
        user_message: The original message from Telegram
        agent_response: The final answer from the agent
        excel_path: Path to the Excel file
        metadata: Optional metadata
        
    Returns:
        Path to the Excel file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create directory if it doesn't exist
    excel_dir = os.path.dirname(excel_path)
    if excel_dir:
        Path(excel_dir).mkdir(parents=True, exist_ok=True)
    
    # Prepare new row data
    new_row = {
        "Timestamp": timestamp,
        "User Message": user_message,
        "Agent Response": agent_response,
    }
    
    if metadata:
        new_row.update(metadata)
    
    # Check if file exists
    if os.path.exists(excel_path):
        # Read existing file
        df = pd.read_excel(excel_path, engine='openpyxl')
        
        # Add new row
        new_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_df], ignore_index=True)
    else:
        # Create new DataFrame
        df = pd.DataFrame([new_row])
    
    # Write back to Excel
    df.to_excel(excel_path, index=False, engine='openpyxl')
    
    return excel_path

