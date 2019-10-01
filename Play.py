# Play the game

import os
import time

from functions import gfunc                     # Game Functions
from classes.menus import Menus                 # Game Menu's
from classes.typing import Typing, bcolors      # Display's typing text
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
    Typing(tspeed, text)

    time.sleep(2)
    text = bcolors.FAIL + bcolors.BOLD + bcolors.UNDERLINE + \
        "\n\n# Tutorial: LOOK #" + bcolors.ENDC
    Typing(tspeed, text)
    input(bcolors.FAIL + ':> ' + bcolors.ENDC)

    text = f'''
{player.usrName} looks around at the {location}
and sees a big tree inside a grass field
surrounded by a man-made wooden fence.
There's a wooden chop-block at the end of the grassfield
next to a stands sturdy man-made wooden log.

A feeling of familiarity came over {player.usrName} as {player.usrGendr[0]} sees
{player.usrGendr[3]} mentor standing in the doorway of the log. '''
    Typing(tspeed, text)

    mentorName = str(
        input(
            f"\n\n{player.usrName} just woke up and rememberd {player.usrGendr[3]} mentor's name..\n:> "))

    while True:
        if mentorName == '':
            text = f"\nIt's been a rough nap... what was {player.usrName}'s mentor's name?'\n"
            Typing(tspeed, text)

            mentorName = str(
                input("\n:> ")).capitalize()
            continue
        else:
            answer = str(
                input((f'\nIs "{mentorName}" correct? (Y/N):\n:> ')).lower())
            if answer == "":
                continue
            elif answer in gfunc.usr_answer[:1]:
                break
            else:
                mentorName = str(
                    input("\nChoose your mentor's name:\n:> ")).capitalize()
                continue
        break

    text = f'''
With a confuced face, {player.usrName}'s {mentorName} walks up to {player.usrGendr[2]}.
He asks {player.usrName} to help him find a map that he burried
somewhere around {location}.

You decide to help {mentorName}.
He places his hand on {player.usrName}'s forehead,
while mumbling some kind of strange mantra.

While listning to the mantra, {player.usrName} can't help but notice,
a strang thermic force comming of {mentorName} body.

Suddenly {mentorName}'s hand glows
and a rainbow-colored thermic force shoots out of his hand ...


A warm feeling came over {player.usrName}.
'''

    text2 = bcolors.FAIL + bcolors.BOLD + f'''=================================
{player.usrGendr[0].capitalize()} accuired the abillity to DIG!
=================================''' + bcolors.ENDC
    time.sleep(3)

    text = f'''
{mentorName} pukes from excaustion!
But he looks happy...
Probably beacuse you can help find his map now.

(((( He tells you its not dig as in shit is under the floor
but you can dig between dimentions.. )))))
'''
    Typing(tspeed, text)

    gfunc.comming_soon()


except KeyboardInterrupt:
    gfunc.quit()
