import logging

def get_logging(name, type, location):
    logger = logging.getLogger(name)
    logger.setLevel(type)

    formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')
    file_handler = logging.FileHandler(location)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger