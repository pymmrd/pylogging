# -*- coding:utf-8 -*-

import logging


def logger_contructor(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create a file handler
    handler = logging.FileHandler('hello.log')
    handler.setLevel(logging.INFO)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    logger = logger_contructor(__name__)
    logger.info('Hello baby')
