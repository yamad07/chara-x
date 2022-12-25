import logging

from pythonjsonlogger import jsonlogger

logger = logging.getLogger("charax")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)

logger.addHandler(handler)
