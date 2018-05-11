# file: config.py
# auth: Libor Wagner <libor.wagner@cvut.cz>

import json
import logging
import collections
import re

log = logging.getLogger("Config")

class Config(collections.UserDict):
    __shared_data = dict()
    def __init__(self, filename=None):
        self.data = self.__shared_data

        if filename is not None:
            self.data.update(json_load_commented(filename))

        if len(self.data):
            log.warn("Empty configuration!")


def json_load_commented(filename, **kvargs):
    with open(filename) as f:
        text = f.read()

    # taken from commentjson (https://github.com/vaidik/commentjson)
    regex = r'\s*(#|\/{2}).*$'
    regex_inline = r'(:?(?:\s)*([A-Za-z\d\.{}]*)|((?<=\").*\"),?)(?:\s)*(((#|(\/{2})).*)|)$'
    lines = text.split('\n')

    for index, line in enumerate(lines):
        if re.search(regex, line):
            if re.search(r'^' + regex, line, re.IGNORECASE):
                lines[index] = ""
            elif re.search(regex_inline, line):
                lines[index] = re.sub(regex_inline, r'\1', line)

    return json.loads('\n'.join(lines), **kvargs)
