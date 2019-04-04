import logging
log_config  =  {
    'filename' : 'error.log',
    'filemode' : 'a+',
    'format' : '%(name)s - %(levelname)s - %(message)s',
    'level' : logging.ERROR
}
logging.basicConfig(**log_config)
logger = logging.getLogger()