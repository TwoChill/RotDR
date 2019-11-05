# Play the game

import os
import time
import base
import engine
import platform
import text

tspeed = 0.05

try:
    engine.sys_clear()

    location = 'Beginning'

    # Gets and prints the game logo.
    Game_Name = engine.game_name()
    base.Typing(0.001, Game_Name)
    time.sleep(2)
    engine.sys_clear()

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

    mentorName = None
    text.game_text(usrName, usrGendr, mentorName, location)

    # Tutorial
    location = 'Home'
    quest = base.Quest(usrName, usrGendr, location)
    quest.tutorial_quest(usrName, usrGendr, location)

except KeyboardInterrupt:
    engine.quit()
