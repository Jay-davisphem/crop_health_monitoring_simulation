import logging

def setup_logger():
    logger = logging.getLogger("CropSimulation")
    logger.setLevel(logging.DEBUG)
    # Create a console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def log_error(error):
    logger = logging.getLogger("CropSimulation")
    logger.error(error)
