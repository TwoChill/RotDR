# Locations
import time
from classes.typing import Typing

# Every first time, there will be a intro text.
# The Intro class should maby not be in this file .. 


class Intro(object):
    def __init__(self, location):
        self.location = location

        ## 0 == frist time // 1 == not first time ##
        # x = 0

        if self.location == 'beginning':

            text = '''
        You are about to embark on a journey of the imagination.
            Full of everything your imagination can fill

                .. With a helping  hand offcourse ..

               .... So let's create a character! ....'''
            Typing(text, 0.05)
            time.sleep(3)

            print('\n\n\n\t\t\t       TO BE CONTINUED')
            time.sleep(4)
            print('\n\n\n\n')
            quit()
            # This is were you will ask usr for input for class Player
