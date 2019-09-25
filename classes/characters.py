# All the characters of the game

import os
import time
import sys
import random
from functions import gfunc                     # Game Functions
from classes.menus import Menus                 # Game Menu's
from classes.typing import Typing               # Display's typing text
from classes.locations import Location

tspeed = 0.05


class Person():
    ''' Holds information and functions that each 'Person' has and can/might do'''

    def __init__(self, hp, mp, atk, df, magic, location):
        self.name = ''
        self.location = location        # Might not be used in this class
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgcl = self.magic[i]['dmg'] - 5
        mgch = self.magic[i]['dmg'] + 5
        return random.randrange(mgcl, mgch)

    def take_damage(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0
        self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]

    def get_spell_mp_cost(self, i):
        self.magic[i]['cost']

    def choose_action(self):
        print('Actions')
        i = 1
        for item in self.actions:
            print(str(i) + ':', item)
            i += 1

    def choose_magic(self):
        print('Magic')
        i = 1
        for spell in self.magic:
            print(str(i) + ':', spell['name'],
                  "costs:", str(spell['cost']) + ')')


class Hero(Person):  # user **kwarg for the backpack / inventory
    '''This class holds information about the player's character'''

    def __init__(self, usrName, usrGendr, location):
        self.usrName = usrName
        self.usrGendr = usrGendr
        self.backpack = {}  # Heres going to Inventory and stuff like that
        self.usr_answer = ('yes', 'y', 'no', 'n')

    def creation(self):
        ''' Creates character name and gender.
        Txt in the game will adapt to the characters gender. '''

        usrGendr = []
        usrGendr_boy = ("he", "his", "him", "his")
        usrGendr_girl = ("she", "hers", "her", "her")
        usr_answer = ('yes', 'y', 'no', 'n')

        # fAI (fake AI) is a list to 'help' the usr to choose a character name.
        fAI = ['\n\t\tJust think of one strong name...\n\n',
               "\n\t\tIt's just a cleaver combination of A's -> Z's ..\n\n",
               "\n\t\t'Zolar'?, 'Matt'?, I'm just trying to help ... \n\n",
               "\n\t\tThere must be something you can think of..\n\n",
               "\n\t\tYes .. It's hard.. and forever. Sooo, take your time..\n\n",
               "\n\t\t..... -_-", "\n\t\tI have faith you'll succeed on your next try.. "]

        usrGendr = str(
            input("\n\t\tAre you a Boy or a Girl?\n\t\t:> ")).lower()

        if usrGendr == 'boy':
            text = '\n\n\t\tA Boy has been created!\n\n'
            Typing(text, tspeed)

            time.sleep(3)
            os.system('clear')

            usrGendr = usrGendr_boy
        elif usrGendr == 'girl':
            text = '\n\n\t\tA Girl has been created!\n\n'
            Typing(text, tspeed)

            time.sleep(3)
            os.system('clear')

            usrGendr = usrGendr_girl
        else:
            # A random gender is choosen.
            randomnr = random.randint(1, 3)

            if randomnr == 1:
                usrGendr = 'boy'
                text = "\n\n\t\tA Boy has been choosen for you.\n\n"
                Typing(text, tspeed)

                time.sleep(3)
                os.system('clear')

                usrGendr = usrGendr_boy
            else:
                usrGendr == 'girl'
                text = "\n\n\t\tA Girl has been choosen for you.\n\n"
                Typing(text, tspeed)

                time.sleep(3)
                os.system('clear')

                usrGendr = usrGendr_girl

        usrName = str(
            input("\n\t\tNow choose your characters Name:\n\t\t:> ")).capitalize()

        while True:
            # len(text) is used because the list above will grow.
            randomnr = random.randint(0, (len(fAI) - 1))

            if usrName == "":
                Typing(fAI[randomnr], tspeed)
                time.sleep(3)

                usrName = str(
                    input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                continue
            else:
                answer = str(
                    input((f'\n\t\tIs "{usrName}" correct? (Y/N):\n\t\t:> ')).lower())

                if answer == "":
                    
                    Typing(fAI[randomnr], tspeed)
                    time.sleep(3)

                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
                elif answer in usr_answer[:2]:

                    os.system('clear')
                    text = '\n\n\t\t{} has born!\n'

                    Typing(text.format(usrName), 0.3)
                    time.sleep(3)
# !
                    gfunc.matrix()
                else:
                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
            break

        return usrName, usrGendr
