# Hello World in Python
# Created for Hacktoberfest 2024

import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


def hello_world():
    for message in ("Hello World! 🌍", "Happy Hacktoberfest!"):
        logging.info(message)

if __name__ == "__main__":
    hello_world()
