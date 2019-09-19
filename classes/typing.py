import sys
import time


class Typing:
    def __init__(self, text, speed):
        self.text = text
        self.speed = speed

        for l in text:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write('\n')
        sys.stdout.flush()