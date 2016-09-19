"""
Author: Aishwarya Sharma
"""

import logging


def get_logger():

    logging.basicConfig(
        filename="debug.log",
        format="[%(asctime)s] - [%(levelname)s] - %(message)s",
        level=logging.DEBUG,
    )
    logger = logging.getLogger()
    return logger
