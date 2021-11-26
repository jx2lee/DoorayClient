import logging

logger = logging.getLogger(__name__)
logger.propagate = False
logger.setLevel(logging.DEBUG)

formatter_pattern = "[%(asctime)s][%(filename)s:%(lineno)s: %(funcName)20s() ] %(message)s"
formatter = logging.Formatter(formatter_pattern)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)