import logging
import os
from datetime import datetime
# Logger configuration for the application
logs_dir = os.path.join(os.getcwd(), "logs") # Directory for logs
os.makedirs(logs_dir, exist_ok=True) # Create logs directory if it does not exist

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Creation of log file with naming convention based on current date and time

##logs_path=os.path.join(logs_dir, LOG_FILE) # Creation of Log file in Current Working Directory

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE) # Full path for the log file
# Logger configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s', #format for log messages
    level=logging.INFO, # Set the logging level to INFO
)

