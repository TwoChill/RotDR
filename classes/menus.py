# Game Menu's

import os
import time
from functions import gfunc                     # Game Functions
from classes.typing import Typing               # Display's typing text


tspeed = 0.005


class Menus(object):
    def __init__(self, location):
        self.location = location
        self.game_name = gfunc.game_name()

    def start_menu(self, location):
        os.system('clear')
        print(self.game_name)
        Welcome_Menu = '''
                        
                        ############################
                        #          Welcome         #
                        ############################

                                  - Play -
                                  - Load -          
                                  - Help -
         
                                  - Quit -
         
                                  Made by:          
                               M.L. de France       
                        ############################
        '''
        Typing(tspeed, Welcome_Menu)
        gfunc.enter_command(location)

    def get_help(self, location):

        if location == 'beginning':
            os.system('clear')
            print(self.game_name)

        Help_Menu = '''

                        ############################
                        #         - Help -         #
                        ############################
                        - Type commands to do them -

                                  - Play -
                        - "play" to start the game -

                                  - Load -
                        - "load" to load your game -

                                  - Quit -
                        - "quit" to exit  the game -

                                 - "back" -


                       - Press "CTRL" to speed  txt -       
                        - Good luck and have fun!! -
                        ############################
        '''
        Typing(tspeed, Help_Menu)
        gfunc.enter_command(location)


# class Spellbook:
