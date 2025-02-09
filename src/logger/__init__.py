import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# Constants for log configuration
LOG_DIR = 'logs'  # Directory where log files will be stored
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Log file name with timestamp
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB - Maximum size of the log file before it rotates
BACKUP_COUNT = 3  # Number of backup log files to keep

# Construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR)  # Get the path of the log directory
os.makedirs(log_dir_path, exist_ok=True)  # Create the directory if it doesn't exist
log_file_path = os.path.join(log_dir_path, LOG_FILE)  # Full path to the log file

def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.
    
    Purpose:
    This function sets up logging for the application, ensuring that logs are captured
    both in the console and in a log file. The log file is rotated when it reaches a 
    maximum size of 5 MB, and up to 3 backup log files are kept.

    The log format includes a timestamp, the logger's name, log level, and the log message.
    
    Author:
    coderRaj07
    
    Creation Date:
    2025-02-09
    """
    # Create a custom logger
    logger = logging.getLogger()  # Get the root logger
    logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG to capture all log levels
    
    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)  # Set the formatter for the file handler
    file_handler.setLevel(logging.DEBUG)  # Set the log level to DEBUG for file handler

    # Console handler
    console_handler = logging.StreamHandler()  # StreamHandler sends log messages to the console
    console_handler.setFormatter(formatter)  # Set the formatter for the console handler
    console_handler.setLevel(logging.INFO)  # Set the log level to INFO for console handler

    # Add handlers to the logger
    logger.addHandler(file_handler)  # Add the file handler to the logger
    logger.addHandler(console_handler)  # Add the console handler to the logger

# Configure the logger
configure_logger()  # Call the function to configure logging
