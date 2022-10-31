import logging


formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')

success_logger = logging.getLogger()
success_logger.setLevel(logging.DEBUG)

success_file_handler = logging.FileHandler('./logs/success.log')
success_file_handler.setFormatter(formatter)

success_logger.addHandler(success_file_handler)

def success_log (str):
   success_logger.debug(str)


fail_logger = logging.getLogger()
fail_logger.setLevel(logging.ERROR)

fail_file_handler = logging.FileHandler('./logs/fail.log')
fail_file_handler.setFormatter(formatter)

fail_logger.addHandler(fail_file_handler)

def fail_log(str):
    fail_logger.debug(str)
    


