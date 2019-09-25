# Play the game

import os
import time

from functions import gfunc                     # Game Functions
from classes.menus import Menus                 # Game Menu's
from classes.typing import Typing               # Display's typing text
# Prints introductions per location
from classes.locations import Location
from classes.characters import Person, Hero

tspeed = 0.05
try:
    os.system('clear')

    location = 'beginning'

    # Gets and prints the game logo.
    Game_Name = gfunc.game_name()
    Typing(Game_Name, 0.001)
    time.sleep(2)
    os.system('clear')

    # Gets the start menu.
    Start_Game = Menus(location)
    Start_Game.start_menu(location)

    location = 'let_there_be_light'

    usrName = ''
    usrGendr = ''

    # Create an instance of Hero with user input
    player = Hero(usrName, usrGendr, location)
    player.creation()

except KeyboardInterrupt:
    gfunc.quit()
