import logging
from os.path import dirname, realpath, pardir, join
from datetime import datetime

"""Logging Configurations"""
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    # Create a file handler
    logPath = join(dirname(realpath(__file__)), pardir, 'logs')
    handler = logging.FileHandler(join(logPath, name.strip('__')+'.log'))
    handler.setLevel(logging.INFO)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s %(funcName)s +%(lineno)s: %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    # add the handler to the logger
    logger.addHandler(handler)

    return logger
