# Play the game

import os
import time
import base as clss
import engine as func
import platform
import text

txtSpeed = 0.05

try:
    func.sys_clear()

    # location = 'Beginning'

    # # Gets and prints the game logo.
    # Game_Name = func.game_name()
    # clss.Typing(0.001, Game_Name)
    # time.sleep(2)
    # func.sys_clear()

    # # Gets the start menu.
    # Start_Game = clss.Menus(location)
    # Start_Game.start_menu(location)

    # # Create an instance of Hero with user input.
    # usrName = ''
    # usrGendr = ()

    # # Create instance of Hero with a NAME and GENDER in var PLAYER
    # player = clss.Hero(usrName, usrGendr, location)
    # player.character_creation()

    # usrGendr = player.usrGendr
    # usrName = player.usrName

    # DEBUG
    usrName = 'Mike'
    usrGendr_Boy = ("he", "his", "him", "his",
                    "He", "His", "Him", "His")
    usrGendr = usrGendr_Boy

    # Calls locator method to track player's location.
    location = 'Home'
    clss.Map.locator(location, True)

    quest = clss.Quest(usrName, usrGendr, location)
    quest.tutorial_quest(usrName, usrGendr, location)

except KeyboardInterrupt:
    func.quit()
