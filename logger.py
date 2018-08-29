import logging


class Logger:

    def __init__(self):
        self.logger = logging.getLogger()
        logging_format = "[%(asctime)s - %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(format=logging_format)
        self.logger.setLevel(level=logging.INFO)
