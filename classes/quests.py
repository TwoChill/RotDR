import os
import time

from functions import gfunc                     # Game Functions
from classes.menus import Menus                 # Game Menu's
from classes.typing import Typing, bcolors      # Display's typing text
from classes.locations import Location
from classes.characters import Person, Hero


class Quest(object):
    def __init__(self, location):
