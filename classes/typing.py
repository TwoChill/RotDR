import sys
import os
import time
import keyboard     # pip install keyboard


class bcolors:
    ''' Text colors to use in the Terminal '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Typing(bcolors):
    ''' Game txt is being typed on screen. CTRL to increase speed '''

    def __init__(self, text, speed):
        self.text = text
        self.speed = speed
        self.bcolors = bcolors

        for l in text:
            if keyboard.is_pressed('ctrl'):
                time.sleep(0.01)
                speed = 0.00001
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(speed)

        sys.stdout.write('\n')
        sys.stdout.flush()

    # create a option to press ENTER and skip the rolling text #
