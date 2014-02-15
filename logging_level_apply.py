# -*- coding:utf-8 -*-

import logging


"""
    In most cases, you don’t want to read too much details in the log file. 
    Therefore, debug level is only enabled when you are debugging. I use 
    debug level only for detail debugging information, especially when the 
    data is big or the frequency is high, such as records of algorithm 
    internal state changes in a for-loop.
"""

def complex_algorithm(items):
    for i, item in enumerate(items):
            # do some complex algorithm computation
                    logger.debug('%s iteration, item=%s', i, item)


"""
    I use info level for routines, for example, handling
    requests or server state changed.
"""
def handle_request(request):
    logger.info('Handling request %s', request)
    # handle request here
    result = 'result'
    logger.info('Return result: %s', result)

def start_service():
    logger.info('Starting service at port %s ...', port)
    service.start()
    logger.info('Service is started')


"""
    I use warning when it is important, but not an error,
    for example, when a user attempts to login with wrong password or connection is slow.
"""

def authenticate(user_name, password, ip_address):
    if user_name != USER_NAME and password != PASSWORD:
        logger.warn('Login attempt to %s from IP %s', user_name, ip_address)
        return False
    # do authentication here


"""
    I use error level when something is wrong, 
    for example, an exception is thrown, IO operation failure or connectivity issue.
"""
def get_user_by_id(user_id):
    user = db.read_user(user_id)
    if user is None:
        logger.error('Cannot find user with user_id=%s', user_id)
        return user
    return user


"""
reference:
  http://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook
"""
