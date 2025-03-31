import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

if __name__=="__main__":
    logging.info("Logging has started")  # This line logs an info message indicating that the logging process has started.
    logging.warning("This is a warning message")  # This line logs a warning message.
    logging.error("This is an error message")  # This line logs an error message.
    logging.critical("This is a critical message")  # This line logs a critical message.