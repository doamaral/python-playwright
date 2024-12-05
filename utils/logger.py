""" Definition of logger object """
import inspect
import logging


def logger(logLevel=logging.DEBUG):
    """ Logger function """
    # Gets the name of the class / method from which this method is called
    logger_name = inspect.stack()[1][3]
    my_logger = logging.getLogger(logger_name)

    # By default, log all messages
    my_logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(filename="test_execution.log", mode='w')
    file_handler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    my_logger.addHandler(file_handler)

    return my_logger
