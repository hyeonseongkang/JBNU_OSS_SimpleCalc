import logging

def get_logging(name, level, location):
    # logger instance 생성
    logger = logging.getLogger(name)
    
    # logger level 설정
    logger.setLevel(level)

    # format 설정
    formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')
    
    file_handler = logging.FileHandler(location)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger