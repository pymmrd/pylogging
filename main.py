# -*- coding:utf-8 -*- 

"""
You can see a lots of example out there (including this article,
I did it just for giving example in short) get logger at module level. 
They looks harmless, but actually, there is a pitfall – Python 
logging module respects all created logger before you load the 
configuration from a file.
And you expect to see the records appear in log, but you will
see nothing. Why? Because you create the logger at module level,
you then import the module before you load the logging configuration from a file. 
The logging.fileConfig and logging.dictConfig disables existing loggers by default.
So, those setting in file will not be applied to your logger.
It’s better to get the logger when you need it. It’s cheap to create or get a logger. 
"""
import logging
import logging.config

# load my module
import my_module

# load the logging configuration
logging.config.fileConfig('logging.ini')

my_module.foo()
bar = my_module.Bar()
bar.bar()

