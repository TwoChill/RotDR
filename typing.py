
# This module is used to indicate how fast or slow the text is being displayed.

import sys
import time


def text_005sec(text):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.005)    # Change this value to change text speed.

    return text


def text_1sec(text):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)    # Change this value to change text speed.

    return text
