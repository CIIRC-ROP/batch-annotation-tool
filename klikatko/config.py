# file: config.py
# auth: Libor Wagner <libor.wagner@cvut.cz>

import json
import logging
import collections

log = logging.getLogger("Config")

class Config(collections.UserDict):
    __shared_data = dict()
    def __init__(self, filename=None):
        self.data = self.__shared_data

        if filename is not None:
            with open(filename) as f:
                self.data.update(json.load(f))

        if len(self.data):
            log.warn("Empty configuration!")
