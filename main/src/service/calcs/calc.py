import logging


class Division:
    log = logging

    def __init__(self):
        self.log.info("Division Constructor")

    def divideBy(self, x, y):
        return x / y
