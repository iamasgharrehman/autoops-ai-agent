# utils/logger.py

import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate a timestamped log file (optional)
log_filename = f"autoops_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_path = os.path.join(LOG_DIR, log_filename)

# Create and configure logger
logger = logging.getLogger("AutoOpsLogger")
logger.setLevel(logging.DEBUG)  # Set to INFO or WARNING in production

# Formatter
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# File handler
file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add handlers if not already added
if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
