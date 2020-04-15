"""
Bite 192. Some logging practice

This is a simple logging exercise. The logging module is very useful and is part of the standard library;
unfortunately it is often neglected by new learners.

You are to flesh out the log_it() function so that it will log to any LOG LEVEL and with any message passed to it.
You will need to create globalvariables for each of the log levels, since those will be imported into the tests for
testing.

LOG LEVELS:
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

By default, all log messages are sent to the root logger, but for this bite you will have to give it the name of
pybites_logger.

You should breeze through this one!
"""


import logging
from typing import Callable

DEBUG = "..."
INFO = "..."
WARNING = "..."
ERROR = "..."
CRITICAL = "..."


def log_it(level: Callable, msg: str) -> None:
    pass


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
