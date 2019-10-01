# Game Locations

import os
import time
from functions import gfunc                     # Game Functions
from classes.typing import Typing               # Display's typing text
from classes.characters import Hero, Person

speed = 0.05

# Every first time, there will be a intro text.
# The Intro class should be a methode instead of a parent class

# REMEBER if only 2 methods in a class.. Don't use classes! or make it a methode / function


class Location(object):
    '''Every location upon first entry, has a introduction'''

    def __init__(self, location):
        self.location = location

    def get_intro(self, location):

        if location == 'beginning':
            os.system('clear')

            text = '''
        You are about to embark on a journey of the imagination.
            Full of everything your imagination can fill

                .. With a helping  hand offcourse ..

               .... So let's create a character! ....'''
            Typing(text, 0.05)
            time.sleep(3)
            os.system('clear')
