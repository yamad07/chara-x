import logging
import sys

from charax.ai import create_response
from charax.logger import logger
from charax.setting import config

if __name__ == "__main__":
    logger.setLevel(logging.ERROR)
    your_name = input("type your name: ")
    bot_name = config["bot"]["name"]

    uttrs = []
    while True:
        message = input("{}: ".format(your_name))
        uttrs.append({"user": your_name, "message": message})

        response = create_response(uttrs, bot_name)
        print("{}: {}".format(config["bot"]["name"], response))
        uttrs.append({"user": bot_name, "message": response})
