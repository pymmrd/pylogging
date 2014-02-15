import logging

######################MODULE LEVEL LOGGER#################

logger = logging.getLogger(__name__)

def foo():
    logger.info('Hi, foo')

class Bar(object):
    def bar(self):
        logger.info('Hi, bar')



###################CREATE LOGGER WHEN YOU NEED#############
"""
import logging

def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')

class Bar(object):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')
"""
