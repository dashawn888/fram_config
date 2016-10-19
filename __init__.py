# -*- coding: utf-8 -*-
"""The standard fram config library.

provides the --config argument and auto parses the file_name passed at the
command line.

To access the values use the standard configparser methods.

https://docs.python.org/2/library/configparser.html
"""
# V2 V3 compatibility
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

__author__ = "Shawn Lee"
__email__ = "shawn@143t.com"


def load_config(file_name):
    """The callback used to load up the config file."""
    if not file_name:
        return
    config = ConfigParser()
    config.readfp(open(file_name))
    return config

FRAM_PLUGIN = {
    "argparse": {
        "--config": {
            "help": "The file name to be parsed by ConfigParser.",
            "callback": load_config,
            "required": True}}}
