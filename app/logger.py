import os
import logging
from logging import handlers


log_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "FATAL": logging.FATAL,
}


if not os.path.exists(os.path.dirname("logs/test.logs")):
    os.makedirs(os.path.dirname("logs/test.logs"))

logger = logging.getLogger("TestProject")
formater = logging.Formatter('%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s')

logger.setLevel(log_level["INFO"])

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formater)
logger.addHandler(stream_handler)

file_handler = handlers.RotatingFileHandler(filename="logs/test.log",
                                            maxBytes=1024*1024*5)
file_handler.setFormatter(formater)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
