# -*- coding:utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG)  #NOTE
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
#DEBUG:__main__:Records: {'john': 55, 'tom': 66}  #NOTE 和info等级不同的是:它显示了info和debug信息 
#INFO:__main__:Updating records ...
#INFO:__main__:Finish updating records
######################################
