# utils/exceptions.py

import traceback
from utils.logger import logger
import traceback
import logging
import sys

# Setup basic logging (you can enhance this)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/autoops.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class AutoOpsError(Exception):
    """Base exception for AutoOps application."""
    def __init__(self, message="An error occurred in AutoOps."):
        self.message = message
        super().__init__(self.message)

class FileOperationError(AutoOpsError):
    """Raised for any file creation, reading, or writing errors."""
    pass

class APIIntegrationError(AutoOpsError):
    """Raised for errors related to external API calls."""
    pass

class WorkflowExecutionError(AutoOpsError):
    """Raised for workflow coordination or task delegation issues."""
    pass

def handle_exception(exc: Exception, context: str = ""):
    exc_type = type(exc).__name__
    logger.error(f"Exception in {context}: [{exc_type}] {str(exc)}")
    logger.debug(traceback.format_exc())
