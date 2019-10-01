# Game Functions

import os
import time
import sys
import random

from classes.menus import Menus                 # Game Menu's
from classes.typing import Typing               # Display's typing text
from classes.locations import Location
from classes.characters import Hero, Person

tspeed = 0.05

usr_answer = ('yes', 'y', 'no', 'n')

# This fAI (fake AI) list are responses given when the user types an unknow command. (Can be expanded upon.)
fAI = ['Uhmm.. I think you misspelled..', "'{}', is kinda.. forein to me.",
       "Nope, I didn't get that!", '.......... -_-',
       'We all have brainfarts sometimes ....', "I don't think '{}' is the answer..",
       'Oeps, brainfart! Again please!', "That's just not correct.",
       "I'm sorry, but I don't know what '{}' means.", "That's what she! said.",
       ".. 'help' could be usefull .."]


def comming_soon():
    time.sleep(1)
    print('\n\t\t\t!! COMMING SOON !!\n')
    time.sleep(4)
    quit()


def enter_command(location):
    ''' Function is used to enter command into the game '''
    if location == 'beginning':

        usr_command = str(input('\t\t\t:> ')).lower()

        if usr_command == 'play':
            Start_Game = Location(location)
            Start_Game.get_intro(location)

        elif usr_command == 'help':
            Help = Menus(location)
            Help.get_help(location)

        elif usr_command == 'load':
            comming_soon()

        elif usr_command == 'back':
            Restart_Game = Menus(location)
            Restart_Game.start_menu(location)

        elif usr_command == 'quit':
            quit()
        else:
            usr_type_error(location, usr_command)
    else:

        usr_command = str(input(':> ')).lower()

        if usr_command == 'look' and location != 'beginning':
            # Class Locations. Per location 1. Intro
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'dig' and location != 'beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'map' and location != 'beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'spellbook' and location != 'beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'save' and location != 'beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'load' and location != 'beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'quit':
            quit()

        else:
            # Uses random answers if usr command is not recognized.
            usr_type_error(location, usr_command)


def usr_type_error(location, usr_command):
    '''Random fake-AI responses for commando errors of the user'''

    randomnr = random.randrange(0, len(fAI))

    # Random answer genereated with TABS for the begin menus of the game (Welcome and Help)
    if location == 'beginning':
        print('\t\t\t' + fAI[randomnr].format(usr_command) + '\n')
        enter_command(location)
    else:
        print(fAI[randomnr].format(usr_command) + '\n')
        enter_command(location)


def game_name():

    game_name = '''
                                _____   _                                
                               |  __ \ (_)                               
                               | |__) | _  ___   ___                     
                               |  _  / | |/ __| / _ \                    
                  __   _    _  | | \ \ | |\__ \|  __/                    
                 / _| | |  | | |_|  \_\|_||___/ \___|                    
           ___  | |_  | |_ | |__    ___                                  
          / _ \ |  _| | __|| '_ \  / _ \                                 
  _____  | (_) || |   | |_ | | | ||  __/    _____   _      _             
 |  __ \  \___/ |_|    \__||_| |_| \___|   |  __ \ (_)    | |            
 | |  | | _ __  __ _   __ _   ___   _ __   | |__) | _   __| |  ___  _ __ 
 | |  | || '__|/ _` | / _` | / _ \ | '_ \  |  _  / | | / _` | / _ \| '__|
 | |__| || |  | (_| || (_| || (_) || | | | | | \ \ | || (_| ||  __/| |   
 |_____/ |_|   \__,_| \__, | \___/ |_| |_| |_|  \_\|_| \__,_| \___||_|   
                       __/ |                                             
                      |___/                                              
'''
    return game_name


def matrix():
    """ Shows "1's" and "0's" in a matrix rain.
    source: https://github.com/nitishpatel"""

    symbols = ["1", "0", " ", " "]  # You can add your alapabets here if needed
    line = []
    counter = 0
    for i in range(118):
        x = random.randint(0, 3)
        line.append(symbols[x])
        counter += 1

    for i in range(150):
        if counter % 5 == 0:
            r_symbols = [random.randint(0, 117)for x in range(10)]
            for i in r_symbols:
                line[i] = symbols[random.randint(0, 3)]
        print(*line)
        time.sleep(0.03)
        counter += 1

    space = '\n' * 40
    Typing(tspeed, space)
    os.system('clear')

    return None


def quit():
    ''' Exits the game with the game logo '''

    os.system('clear')

    text = '''
                            Thank you for playing!'''
    Typing(tspeed, text)

    Game_Name = game_name()
    Typing(tspeed, Game_Name)

    sys.exit()
