# Play the game

import time
import base as clss
import engine as func
import platform
import text as gameText

txtSpeed = 0.05

usrName = ''
usrName_Plural = ''
usrGendr = ()

try:
    func.sys_clear()

    # # DEBUGGING block
    # usrName = 'Mike'
    # usrGendr_Boy = ("he", "his", "him", "his",
    #                 "He", "His", "Him", "His")
    # usrGendr = usrGendr_Boy

    location = 'Beginning'

    # Gets and prints the game logo.
    Game_Name = gameText.game_name
    clss.Typing(0.0005, Game_Name)
    time.sleep(2)
    func.sys_clear()

    # Gets the start menu.
    Start_Game = clss.Menus(location)
    Start_Game.start_menu(location)

    # Create and holds players info
    player = clss.Hero(usrName, usrGendr, location)
    usrInfo = player.character_creation()

    usrName = [usrInfo[0], usrInfo[1]]
    usrGendr = usrInfo[2]

    # Calls 'locator' method to track player's location.
    location = 'Home'
    clss.Map.locator(location, True)

    start = clss.Quest(usrName, usrGendr, location)
    start.tutorial_quest(usrName, usrGendr, location)

except KeyboardInterrupt:
    func.quit()
