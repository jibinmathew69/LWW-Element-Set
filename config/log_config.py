'''
This module contains the logging configurations and the logger object
'''
import logging
LOG_CONFIG = {
    'filename' : 'log/error.log',
    'filemode' : 'a+',
    'format' : '%(name)s - %(levelname)s - %(message)s',
    'level' : logging.ERROR
}
logging.basicConfig(**LOG_CONFIG)
LOGGER = logging.getLogger()
