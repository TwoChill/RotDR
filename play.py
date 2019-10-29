# Play the game

import os
import time
import base
import engine


time.sleep(3)

tspeed = 0.05

try:
    os.system('clear')

    location = 'beginning'

    # Gets and prints the game logo.
    Game_Name = engine.game_name()
    base.Typing(0.001, Game_Name)
    time.sleep(2)
    os.system('clear')

    # Gets the start menu.
    Start_Game = base.Menus(location)
    Start_Game.start_menu(location)

    # Create an instance of Hero with user input.
    usrName = ''
    usrGendr = ()

    # Create instance of Hero with a NAME and GENDER in var PLAYER
    player = base.Hero(usrName, usrGendr, location)
    player.character_creation()

    usrGendr = player.usrGendr
    usrName = player.usrName

    # Tutorial
    location = 'garden'
    quest = base.Quest(usrName, usrGendr, location)
    quest.tutorial(usrName, usrGendr, location)

except KeyboardInterrupt:
    engine.quit()
