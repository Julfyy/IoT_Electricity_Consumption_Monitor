import logging

def setup_logger():
    logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s %(message)s")

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
