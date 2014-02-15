# -*- coding:utf-8 -*-

import os
from handler_logging import logger_contructor

def print_traceback():
    """
    By calling logger methods with exc_info=True parameter,
    traceback is dumped to the logger. 
    """
    logger = logger_contructor(__name__)
    try:
        open('/path/to/data/doc.file', 'rb')
    except IOError, e:
        logger.info('%s' % os.linesep)
        logger.error('failed to open file', exc_info=True) # I
        #logger.exception('failed to open file') # II (I==II)

if __name__ == "__main__":
    print_traceback()


#######################结果形式#####################
#2014-02-15 12:04:02,186 - __main__ - INFO - 
#
#2014-02-15 12:04:02,186 - __main__ - ERROR - failed to open file
#Traceback (most recent call last):
#  File "trackback_logging.py", line 9, in print_traceback
#    open('/path/to/data/doc.file', 'rb')
#IOError: [Errno 2] No such file or directory: '/path/to/data/doc.file'
