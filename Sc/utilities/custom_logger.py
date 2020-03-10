import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
import os
import sys

import json
from easydict import EasyDict
from pprint import pprint

def setup_logging(log_dir):

    log_file_format = "[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d"
    log_console_format = "[%(levelname)s]: %(message)s"
    path = "/home/delixus/Downloads/New folder-20200129T110129Z-001/New folder/Sc/venv/logs/"

    print(path)




    # Main logger
    main_logger = logging.getLogger()
    main_logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(Formatter(log_console_format))

    exp_file_handler = TimedRotatingFileHandler(path+'{}_exception.log'.format(log_dir))
    exp_file_handler.setLevel(logging.INFO)
    exp_file_handler.setFormatter(Formatter(log_file_format))

    exp_errors_file_handler = TimedRotatingFileHandler(path+'{}_error.log'.format(log_dir))
    exp_errors_file_handler.setLevel(logging.INFO)
    exp_errors_file_handler.setFormatter(Formatter(log_file_format))

    main_logger.addHandler(console_handler)
    main_logger.addHandler(exp_file_handler)
    main_logger.addHandler(exp_errors_file_handler)

