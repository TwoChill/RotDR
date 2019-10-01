# All the characters of the game

import os
import time
import sys
import random
from functions import gfunc                     # Game Functions
from classes.menus import Menus                 # Game Menu's
from classes.typing import Typing               # Display's typing text

# usrName = ''
# usrGendr = ''

usrGendr = []
usr_answer = ('yes', 'y', 'no', 'n')

tspeed = 0.05


class Person(object):
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
        #super().__init__(hp, mp, atk, df, magic, location)
        self.usrName = ''
        self.usrGendr = ''
        self.backpack = {}  # Here's going to Inventory and stuff like that
        self.inventory = ''  # gfunc.get_inventory

    def character_creation(self):
        ''' Creates character name and gender.
        Txt in the game will adapt to the characters gender. '''

        usrGendr_boy = ("he", "his", "him", "his",
                        "He", "His", "Him", "His")
        usrGendr_girl = ("she", "hers", "her", "her",
                         "She", "Hers", "Her", "Her")

        # This fAI (fake AI) list is seperate because of the display tabs.
        fAI_CC = ['\n\t\tJust think of one strong name...\n\n',
                  "\n\t\tIt's just a cleaver combination of A's -> Z's ..\n\n",
                  "\n\t\t'Zolar'?, 'Matt'?, I'm just trying to help ... \n\n",
                  "\n\t\tThere must be something you can think of..\n\n",
                  "\n\t\tYes .. It's hard.. and forever. Sooo, take your time..\n\n",
                  "\n\t\t..... -_-", "\n\t\tI have faith you'll succeed on your next try.. ",
                  "\n\t\tIt's a thing now-a-day's.. Just pick on for the naritave of the game ;)\n\n"]

        usrGendr = str(
            input("\n\t\tAre you a Boy or a Girl?\n\t\t:> ")).lower()

        while True:

            if usrGendr == 'boy':
                text = '\n\n\t\tA Boy has been created!\n\n'
                Typing(tspeed, text)

                time.sleep(3)
                os.system('clear')

                usrGendr = usrGendr_boy
            elif usrGendr == 'girl':
                text = '\n\n\t\tA Girl has been created!\n\n'
                Typing(tspeed, text)

                time.sleep(3)
                os.system('clear')

                usrGendr = usrGendr_girl
            else:
                randomnr = random.randint(0, len(fAI_CC) - 1)
                Typing(tspeed, fAI_CC[randomnr])
                time.sleep(3)
                os.system('clear')

                usrGendr = str(
                    input("\n\t\tAre you a Boy or a Girl?\n\t\t:> ")).lower()
                continue
            break

        usrName = str(
            input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()

        while True:
            # len(text) is used because the list above will grow.
            randomnr = random.randint(0, (len(fAI_CC) - 1))

            if usrName == "":
                Typing(tspeed, fAI_CC[randomnr])
                time.sleep(3)
                os.system('clear')

                usrName = str(
                    input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                continue
            else:
                answer = str(
                    input((f'\n\t\tIs "{usrName}" correct? (Y/N):\n\t\t:> ')).lower())

                if '' == answer in usr_answer[2:]:

                    Typing(tspeed, fAI_CC[randomnr])
                    time.sleep(3)
                    os.system('clear')

                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
                elif answer in usr_answer[:2]:
                    os.system('clear')
                    text = '\n\n\t\t{} has been created!\n\n\tInitialization: Started\n\nInitialize in:\n3 ...\n2 .. \n1 . \n'

                    Typing(0.1, text.format(usrName))
                    time.sleep(1)

                    gfunc.matrix()
                else:
                    os.system('clear')
                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
            break

        self.usrName = usrName
        self.usrGendr = usrGendr

    def get_inventory(self):
        '''Function to see what and how many items the player has'''

        pass

    def look(self):
        '''The player can look around'''
        # call class
        pass


class Enemy(Person):
    # This class inherites all the metods and attributs from its parent class
    pass
