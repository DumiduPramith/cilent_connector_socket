import logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
def set_logger(logger_name,log_file="log/info.log", level=logging.DEBUG):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger