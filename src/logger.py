import logging
import os
from datetime import datetime

# Create a directory for logs if it doesn't exist. it creates a directory named 'logs' in the current working directory.
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True) # makes sure even if the file exists, it will keep appending


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# .basicconfig allows us to set basic configurations like logging level and log message format for an entire application. 
# also provides a quick way to configure the root logger, used for handling several common logging scenarios.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s', # lineno is the line number where the log message was generated, names is the name of the logger that generated the log message, levelname is the level of the log message (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL), and message is the actual log message.
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")  # checking if logging is working