import game_functions
import time
import os
import player_location
false = False


def tutorial_quest(usrName, usrGendr, location):
    os.system('clear')

    location = 'Garden'
    bool = false

    text = f'''
{usrName} slowly opens {usrGendr[3]} eyes from {usrGendr[3]} hammock.

The first thing {usrName} notice
is the warm sun on {usrGendr[2]} face
birds chirping faintly in the background
and a lukewarm breeze,
that carries a sweet scent of primrose roses.

Afther a few seconds
you hear the sound of a door opening.
You look up and see your mentor standing in a doorway.
'''
    game_functions.typing_text(text)  # Makes the tekst seems like it's typing

    time.sleep(1)
    print("\n\n# Tutorial: LOOK #")
    time.sleep(2)
    print("\nType 'look' to look around")

    input(":> ")

    text = f'''
{usrName} looks around at {location}
and sees a big tree inside a grass field
surrounded by a man-made wooden fence.
There's a wooden chop-block at the end of the grassfield
next to a stands sturdy man-made wooden log.

A feeling of familiarity came over {usrName} as {usrGendr[0]} sees
{usrGendr[3]} mentor standing in the doorway of the log. '''

    mentorName = str(
        input(
            f"\n\n{usrName} just woke up and can't remember {usrGendr[3]} mentor's name..\n:> "))

    text_2 = f'''
With a confuced face, {usrName}'s {mentorName} walks up to {usrGendr[2]}.
He asks {usrName} to help him find a map that he burried
somewhere around {location}.

You decide to help {mentorName}.
He places his hand on {usrName}'s forehead,
while mumbling some kind of strange mantra.

While listning to the mantra, {usrName} can't help but notice,
a strang thermic force comming of {mentorName} body.

Suddenly {mentorName}'s hand glows
and a rainbow-colored thermic force shoots out of his hand ...

<<<break up code to slow these tekst>>>

A warm feeling came over {usrName}.

=================================
{usrGendr[0].capitalize()} accuired the abillity to DIG!
=================================
<<<break up code to slow these tekst>>>

{mentorName} pukes from excaustion!
But he looks happy...
Probably beacuse you can help find his map now.

(((( He tells you its not dig as in shit is under the floor
but you can dig between dimentions.. )))))
'''
    game_functions.typing_text(text)       # Makes the tekst seems like it's typing
    game_functions.typing_text(text_2)     # Makes the tekst seems like it's typing

    time.sleep(1)
    print("\n\n# Tutorial DIG #")
    time.sleep(2)
    print("\nType 'dig' to dig for the map.")

    input(':> ')

    text = f'''
{usrName} puts {usrGendr[3]} hand to the ground..
and {usrGendr[0]} opens somehow a small portal
with the same rainbow-colored thermic force from her hand.

{usrGendr[0]} went through the ground's dimension and felt something...

It was the map {mentorName} was looking for.
{usrName} turns around and gives the map to {usrGendr[3]} mentor.

With relieve {mentorName} looks at the map
and with a snap of his fingers it vanishes .. !?!

{mentorName} looks a {usrName} and ask to use the map ..
'''
    game_functions.typing_text(text)   # Makes the tekst seems like it's typing

    time.sleep(1)
    print("\n\n\n# Tutorial: MAP #")
    time.sleep(2)
    print("\nType 'map' to see the map")

    input(':> ')

    print(f'\n\n{usrName} looks at map!\n')  # Change tekst to how it appears
    player_location.land_map(usrName, usrGendr, location, bool)

# def spellbook_quest():
#     # everything about this quest
#     # if quest is done.. msg for some thing else
#     # secondary action is for t stone
#
# def wand_quest():
#     # everything about this quest
#     # have to dig
#
# def invisableCloak_quest():
#     # everything about this quest
#     # can use w to obtain but this evil act will cause cloak to be dark
#     # and gets banashed from dragon riders land for ever

# def princess_tower():
#     # can hear princess
#     # lock opens depends on items
#     #
#
