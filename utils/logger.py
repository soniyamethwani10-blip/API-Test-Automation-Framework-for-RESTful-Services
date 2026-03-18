import logging
import os
from datetime import datetime

class Logger:
    _logger = None

    @staticmethod
    def get_logger():
        if Logger._logger is None:
            # Create logs directory if it doesn't exist
            log_dir = os.path.join(os.getcwd(), "logs")
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # Define log filename with timestamp
            log_filename = f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
            log_filepath = os.path.join(log_dir, log_filename)

            # Create logger
            logger = logging.getLogger("API_Framework")
            logger.setLevel(logging.DEBUG)

            # Create handlers
            c_handler = logging.StreamHandler()
            f_handler = logging.FileHandler(log_filepath)
            
            c_handler.setLevel(logging.INFO)
            f_handler.setLevel(logging.DEBUG)

            # Create formatters and add to handlers
            log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            c_handler.setFormatter(log_format)
            f_handler.setFormatter(log_format)

            # Add handlers to the logger
            logger.addHandler(c_handler)
            logger.addHandler(f_handler)
            
            Logger._logger = logger

        return Logger._logger

# Global logger instance
logger = Logger.get_logger()
