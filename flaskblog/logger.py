import logging

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    file_handler = logging.FileHandler(log_file)        
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
