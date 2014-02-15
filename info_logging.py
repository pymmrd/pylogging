# -*- coding:utf-8 -*-

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
logger.info('Finish updating records')


#####################################
#result:
#INFO:__main__:Start reading database
#INFO:__main__:Updating records ...
#INFO:__main__:Finish updating records
######################################
