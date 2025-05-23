import logging

logger = logging.getLogger("generator_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
