# Play the game

import os
import time

from functions import gfunc                     # Game Functions
from classes.menus import Menus                 # Game Menu's
from classes.typing import Typing               # Display's typing text
from classes.locations import Location
from classes.characters import Person, Hero

tspeed = 0.05

try:
    os.system('clear')

    location = 'beginning'

    # # Gets and prints the game logo.

    # Game_Name = gfunc.game_name()
    # Typing(Game_Name, 0.001)
    # time.sleep(2)
    # os.system('clear')

    # # Gets the start menu.
    # Start_Game = Menus(location)
    # Start_Game.start_menu(location)

    # Create an instance of Hero with user input.
    usrName = ''
    usrGendr = ''

    player = Hero(usrName, usrGendr, location)
    player.character_creation()

    # Intro Home
    location = 'garden'

    text = f'''
{player.usrName} slowly opens {player.usrGendr[3]} eyes from {player.usrGendr[3]} hammock.

The first thing {player.usrName} notice
is the warm sun on {player.usrGendr[3]} face,
birds chirping faintly in the background,
and a lukewarm breeze,
that carries a sweet scent of primrose roses.

Peacefull..



Afther a few moments,
{player.usrName} hears the sound of a door opening.
{player.usrGendr[4]} looks up and sees {player.usrGendr[3]} mentor standing in a doorway.
'''
    Typing(text, tspeed)

    gfunc.comming_soon()


except KeyboardInterrupt:
    gfunc.quit()
