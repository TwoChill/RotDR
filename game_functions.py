import os
import random
import time
import player_quests
import player_location
import typing


usrGendr = []
usrGendr_boy = ["he", "his", "him", "his"]
usrGendr_girl = ["she", "hers", "her", "her"]


def enter_command(usrName, usrGendr, location, ):

    usr_command = str(input(':> ')).upper()

    if usr_command == 'LOOK':
        player_location.look(usrName, usrGendr, location)

    elif usr_command == 'DIG':
        player_location.dig(usrName, usrGendr, location)

    elif usr_command == 'MAP':
        player_location.land_map(usrName, usrGendr, location)

    elif usr_command == 'HELP':
        help(location)
        # return usrName, usrGendr, location, usr_command
    else:
        return usr_command


def player_info(usrName, usrGendr, location):

    text = '''
You are about to embark on a journey of the imagination.
Full of everything your imagination can fill ...

.. With a helping hand offcourse ..

.... So let's create a character ....
'''
    typing.text_005sec(text)

    usrGendr = str(input("\n\nWill you be playing as a Boy or a Girl?\n:> ")).upper()

    if usrGendr == 'BOY':
        text = '\n\nA Boy has been created!\n\n'
        typing.text_005sec(text)
        usrGendr = usrGendr_boy
    elif usrGendr == 'GIRL':
        text = '\n\nA Girl has been created!\n\n'
        typing.text_005sec(text)
        usrGendr = usrGendr_girl
    else:
        randomnr = random.randint(1, 3)

        if randomnr == 1:
            usrGendr = 'BOY'
            text = "\n\nI think I'll make a Boy for you.\n\n"
            typing.text_005sec(text)
            usrGendr = usrGendr_boy
        else:
            usrGendr == 'GIRL'
            text = "\n\nI think I'll make a Girl for you.\n\n"
            typing.text_005sec(text)
            usrGendr = usrGendr_girl

    usrName = str(input("\nNow choose your characters Name:\n:> ")).capitalize()

    while True:
        if usrName == "":
            text = '\nI just need one strong name...\n'
            typing.text_005sec(text)
            usrName = str(
                input("\nChoose your characters name:\n:> ")).capitalize()
            continue
        else:
            answer = str(
                input((f'\nIs "{usrName}" correct? (Y/N):\n:> ')).upper())
            if answer == "":
                continue
            elif (answer == 'Y') or (answer == 'YES'):
                time.sleep(1)
                os.system('clear')
                player_quests.tutorial_quest(usrName, usrGendr, location)
            elif (answer == 'N') or (answer == 'NO'):
                usrName = str(
                    input("\nChoose your characters name:\n:> ")).capitalize()
                continue
            else:
                continue
        break
    return usrName, usrGendr


def start(usrName, usrGendr, location):
    print('\n############################')
    print('# Rise of the Dragon Rider #')
    print('############################\n')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('\n          Made by:          ')
    print('       M.L. de France       ')
    print('\n############################\n')

    usr_command = str(input(':> ')).upper()

    os.system('clear')                         # Will clear the terminal

    if usr_command == 'PLAY':
        os.system('clear')                      # Will clear the terminal
        player_info(usrName, usrGendr, location)
    elif usr_command == 'HELP':
        help(location)
    elif usr_command == 'QUIT':
        quit()
    else:
        print('\nI didn\'t get that!\n')


def help(usrName, location):
    if location == "beginning":
        print('\n############################')
        print('#         - Help -         #')
        print('############################\n')
        print('- Type your commands to do them.\n')
        print('- Type "play" to start the game.')
        print('- Type "quit" to quit the game.')
        print('- Other commands available soon.\n')
        print('- Good luck and have fun!.')
        print('\n############################')

        str(input('\nOr press ENTER to continue\n\n:>'))

        os.system('clear')
        start(usrName, usrGendr, location)

    # else:       # This else statement should hold the full help sentences:
    #     print('\n\n############################')
    #     print('#         - Help -         #')
    #     print('############################\n')
    #     print('- Type your commands to do them.\n')
    #     print('- Use "look" to inspect area.')
    #     print('- Use "dig" to investigate area.')
    #     print('- Use "map" to see area.\n')
    #     print('- Good luck and have fun!.')
    #     print('\n############################')
    #     while True:
    #         if usr_answer == "":
    #             game_functions.start(usrName, usrGendr, location)
    #         else:
    #             usr_answer = str(input('\nJust ENTER or the BACKSPACE is enough.\n:>'))


def intro_setting(usrName, location):

    dic_intros = {
        'Home': f'''\n{location} INTRO HERE\n'''.upper(),
        'Garden': f'''\n{location} INTRO HERE\n'''.upper(),
        'usrName_room': f'''\n{location} INTRO HERE\n'''.upper(),
        'Wildland': f'''\n{location} INTRO HERE\n'''.upper(),
        'North': f'''\n{location} INTRO HERE\n'''.upper(),
        'North_West': f'''\n{location} INTRO HERE\n'''.upper(),
        'West': f'''\n{location} INTRO HERE\n'''.upper(),
        'South_West': f'''\n{location} INTRO HERE\n'''.upper(),
        'South': f'''\n{location} INTRO HERE\n'''.upper(),
        'South_East': f'''\n{location} INTRO HERE\n'''.upper(),
        'East': f'''\n{location} INTRO HERE\n'''.upper(),
        'DarkLands': f'''\n{location} INTRO HERE\n'''.upper(),
    }
    intro_setting = dic_intros.get(location)
    return intro_setting


def quit():
    text = '\nThank you for playing Rise of the Dragon Rider!\n'
    typing.text_005sec(text)
    exit(0)

# def game_over():
#     # depending on how, game over msg is displayd
#     # can coninue from last save or auto_save (which is every room enter)
#
# def save_game():
#     # saves items, qeusts done, progression order
#     # saves game manualy
#     # ask to overwrite or create new save.
#
# def auto_save():
#     # auto saves afther certain points and quests
#     # auto saves every room entry.
#
# def mentor(location, quest1, quest2, quest3,):
#     location = Home
#     # parameter tells were you are in game and what to print
#     # go outside and inside get basic_quest to dig outside find map() for mentor.
#     ##got_quest = True (and shows in menu)
#     # asked about quest and gives a hint an what to do next?
# def shoptrader(location):
#     location = 'Wildland'
#     # first static at calmlands()
#     # later based on player location moves around inc 3 or 4.
#     # when shoptraders moves, has found mysterious stone, gives it to you for some gil
#     # combine items to get new items wich can be used to do maby secret things
#
# def progression():
#     # keeps a record of the main story so far
#     # order can change depending on how the game is played.
#
#
# def lore_books(location, book_nr):
#     # book_nr == 1:
#     #   print(''' Book 1 ''')
#     #  etc
#     # some books are only found through digging
#
# def menu(got_quest, got_spellbook, lorefound):
#     # when called shows a list of things to click
#     # when click on inventory, when accesd from here, show list of items in inventory in inv().
#     # inventory()
#     # map()
#    # show map if possible
#     # quests()
#     # Spellbook()
#    #   only availibe afther the quest
#     # lore_books('all')
#     # Progression
#     # Save game
#     # Exit Game
#     # help
#     # q to quit
