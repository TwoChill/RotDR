import os
import time
import sys
import random
import keyboard  # pip install keyboard
import engine as func
import platform
import text as gameText

txtSpeed = func.txtSpeed
txtWait = func.txtWait

usrNameColor = 'orange'
usrAnswer = func.usrAnswer
usrGendr_Boy = func.usrGendr_Boy
usrGendr_Girl = func.usrGendr_Girl

mentorNameColor = func.mentorNameColor


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
        # super().__init__(hp, mp, atk, df, magic)
        self.usrName = ''
        self.usrName_Plurar = ''
        self.usrGendr = ''

        self.backpack = {}  # Here's going to Inventory and stuff like that

    def character_creation(self):
        ''' Creates Hero's name and gender.
        Txt in the game will adapt to the Hero's gender. '''

        fAI_CC = gameText.fAI_CC

        usrGendr = str(
            input("\n\t\tAre you a Boy or a Girl?\n\t\t:> ")).lower()

        while True:

            if usrGendr == 'boy':
                Typing(
                    txtSpeed, Typing.text_decor('white',
                                                gameText.createBoy, 'bold'))

                time.sleep(txtWait)
                func.sys_clear()
                usrGendr = usrGendr_Boy
            elif usrGendr == 'girl':
                Typing(
                    txtSpeed, Typing.text_decor('white',
                                                gameText.createGirl, 'bold'))

                time.sleep(txtWait)
                func.sys_clear()

                usrGendr = usrGendr_Girl
            elif usrGendr in ('gender-neutral', 'gender neutral'):
                Typing(txtSpeed, gameText.fAI_CC[:-1])

                randomnr = random.randint(1, 3)

                if randomnr == 1:
                    Typing(txtSpeed, Typing.text_decor(
                        None, gameText.createBoy, 'bold'))
                    time.sleep(txtWait)
                    func.sys_clear()
                else:
                    Typing(txtSpeed, Typing.text_decor(
                        None, gameText.createGirl, 'bold'))
                    time.sleep(txtWait)
                    func.sys_clear()
            else:
                randomnr = random.randint(0, (len(fAI_CC) - 1) - 1)
                Typing(txtSpeed, fAI_CC[randomnr])
                time.sleep(txtWait)
                func.sys_clear()

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
                Typing(txtSpeed, fAI_CC[randomnr])
                time.sleep(txtWait)
                func.sys_clear()

                usrName = str(
                    input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                continue
            else:
                answer = str(
                    input((f'\n\t\tIs "{usrName}" correct? (Y/N):\n\t\t:> ')).lower())

                if '' == answer in usrAnswer[2:]:

                    Typing(txtSpeed, fAI_CC[randomnr])
                    time.sleep(txtWait)
                    func.sys_clear()

                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
                elif answer in usrAnswer[:2]:
                    func.sys_clear()
                    text = '\n\n\t\t{} has been created!\n\n\tInitialization: Started\n\nInitialize in:\n3 ...\n2 .. \n1 . \n'

                    Typing(0.05, text.format(usrName))
                    time.sleep(txtWait)

                    func.matrix()
                else:
                    func.sys_clear()
                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
            break

        usrName_Plurar = usrName + "'s"

        return Typing.text_decor(usrNameColor, usrName, 'bold'), Typing.text_decor(usrNameColor, usrName_Plurar, 'bold'), self.usrGendr

    def get_backpack(self):
        '''Function to see what and how many items the player has'''
        pass

    def look(self):
        '''The player can look around'''
        # call class or
        pass


class Mentor(Person):
    ''' This is the mentor class. Should be able to fight later in the game'''

    def __init__(self, mentorName):
        # super().__init__(hp, mp, atk, df, magic)
        self.mentorName = mentorName

    def get_name(self, usrName, usrGendr):
        mentorName = str(
            input(
                f"\n\n{usrName} just woke up and rememberd {usrGendr[3]} mentor's name..\n:> "))

        while True:
            if mentorName == '':
                text = f"\nIt's been a rough nap... what was {usrName}'s mentor's name?'\n"
                Typing(txtSpeed, text)

                mentorName = str(
                    input("\n:> ")).capitalize()
                continue
            else:
                answer = str(
                    input((f'\n"{mentorName}"? That sounds about right.. (Y/N):\n:> ')).capitalize())
                if answer == "":
                    continue
                elif answer.lower() in usrAnswer[:2]:
                    break
                else:
                    mentorName = str(
                        input("\nChoose your mentor's name:\n:> ")).capitalize()
                    continue
            break

        mentorName_Plurar = mentorName + "'s"

        return Typing.text_decor(mentorNameColor, mentorName, 'bold'), Typing.text_decor(mentorNameColor, mentorName_Plurar, 'bold')


class Enemy(Person):
    # This class inherites all the metods and attributs from its parent class
    pass

# Every first time, there will be a intro text.
# The Intro class should be a methode instead of a parent class

# REMEBER if only 2 methods in a class.. Don't use classes! or make it a methode / function


class Location(object):

    def __init__(self, location):
        self.location = location

    def get_intro(self, location):
        '''Every location upon first entry, has a introduction'''

        if location == 'Beginning':
            func.sys_clear()

            text = '''
            You are about to embark on a journey of the imagination.
                Full of everything your imagination can fill

                    .. With a helping  hand offcourse ..

                   .... So let's create a character! ....'''
            Typing(0.05, text)
            time.sleep(txtWait)
            func.sys_clear()


class Menus(object):
    def __init__(self, location):
        self.location = location
        self.game_name = func.game_name()

    def start_menu(self, location):
        ''' The start menu with options for the player '''
        func.sys_clear()
        print(self.game_name)

        Typing(0.005, gameText.Welcome_Menu.format(
            'Welcome', 'Play', 'Load',
            'Help', 'Quit', 'M.L. de France'))
        func.enter_command(location)

    def get_help(self, location):
        ''' The help menu with tips about the game '''

        if location == 'Beginning':
            func.sys_clear()
            print(self.game_name)

            Typing(0.005, gameText.Help_Menu.format(
                'Play', 'Load', 'Quit', "back"))
            func.enter_command(location)
        else:
            Typing(0.005, gameText.Help_Menu.format(
                'Play', 'Load', 'Quit', "back"))
            func.enter_command(location)

    def get_spellbook():
        pass

    def save_game():
        pass

    def load_game():
        pass


# class Spellbook:

class dig:

    def __init__(self, usrName, usrGendr, location):
        self.usrName = usrName
        self.usrGendr = usrGendr
        self.location = location
        print('dig Fucntionn')


class Look:
    def __init__(self, usrName, usrGendr, location):
        self.usrName = usrName
        self.usrGendr = usrGendr
        self.location = location


class bcolors(object):
    ''' Text colors to use in the Terminal '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Typing(bcolors):
    ''' Game txt is being typed on screen. CTRL to increase speed '''

    def __init__(self, speed, text=None):
        self.text = text

        if text is None:
            self.text == []
        else:
            self.text = text

        self.speed = speed
        self.bcolors = bcolors

        text = ''.join(self.text)

        for l in text:
            # This block lets player press CTRL and skip the rolling of text #
            if keyboard.is_pressed('ctrl'):
                time.sleep(0.01)
                speed = 0.00001
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(speed)

        sys.stdout.write('\n')
        sys.stdout.flush()

    @classmethod
    def text_decor(cls, color, text=None, decor=None):
        ''' This function decorates text with UNDERLINE and/or BOLD '''

        if color == 'red':
            text = bcolors.FAIL + text + bcolors.ENDC
        elif color == 'green':
            text = bcolors.OKGREEN + text + bcolors.ENDC
        elif color == 'blue':
            text = bcolors.OKBLUE + text + bcolors.ENDC
        elif color == 'orange':
            text = bcolors.WARNING + text + bcolors.ENDC
        else:
            text = text

        for i in decor:
            if i == 'underline':
                text = bcolors.UNDERLINE + text + bcolors.ENDC

            if i == 'bold':
                text = bcolors.BOLD + text + bcolors.ENDC

        return text


class Quest(Hero):

    def __init__(self, usrName, usrGendr, location):
        super().__init__(usrName, usrGendr, location)

    def tutorial_quest(self, usrName, usrGendr, location):
        time.sleep(txtWait)

        mentorName = ''

        Typing(txtSpeed, gameText.tutorial_text_1.format(
            usrName, usrGendr[3], usrGendr[3], usrName, usrGendr[3], usrName, usrGendr[4], usrGendr[3]))

        # Player obtains the ability 'LOOK'
        func.obtains('LOOK', usrName)
        func.cmd_tutorial('look')
        func.sys_clear()

        Typing(txtSpeed, gameText.tutorial_text_2.format(
            usrName, location, usrName, usrGendr[0], usrGendr[3]))
        time.sleep(txtWait)

        # Player chooses Mento's name.
        mentor = Mentor(mentorName)
        mentorName = mentor.get_name(usrName, usrGendr)
        func.sys_clear()

        Typing(txtSpeed, gameText.tutorial_text_3.format(
            mentorName[0], usrName, location,
            mentorName[0], usrName[1], usrName,
            mentorName[0], mentorName[1], usrName))

        # Player obtains the ability 'DIG'
        func.obtains('DIG', usrName)
        func.cmd_tutorial('dig')
        func.sys_clear()

        Typing(txtSpeed, gameText.tutorial_text_4.format(
            mentorName[0], usrName, usrGendr[3],
            usrGendr[3], usrName, usrName[1],
            usrGendr[0]))

        time.sleep(3)
        Typing(txtSpeed, gameText.tutorial_text_5.format(
            mentorName[0]))

        time.sleep(4)
        func.sys_clear()

        Typing(txtSpeed, gameText.tutorial_text_6.format(
            usrName, usrGendr[3], mentorName[0],
            mentorName[0], usrName, usrGendr[2]))

        # Player obtains the 'MAP'
        func.obtains('MAP', usrName)
        func.cmd_tutorial('map')

        first_entered = False
        map = Map(usrName, usrGendr, location)
        map.get_map(usrName, usrGendr, location, first_entered)

        func.comming_soon()

    def quest1(self):
        pass

    def quest2(self):
        pass

    def quest3(self):
        pass

    def quest4(self):
        pass


class Map(Hero):
    def __init__(self, usrName, usrGendr, location):
        super().__init__(usrName, usrGendr, location)

    def get_map(self, usrName, usrGendr, location, first_entered):
        ''' Holds a record of were player has been and shows it on a map '''
        self.location = location
        self.first_entered = first_entered

        # Create new instance to separate keys en values of dict in static 'locator' methode
        # map = Map(usrName, usrGendr, location)

        # This block creates a new dictionary with boolean values ​​corresponding with visited places by placer.
        getKeys = Map.locator(location, first_entered).keys()
        getValues = Map.locator(location, first_entered).values()
        getKeysAndValues = {key: value for key,
                            value in zip(getKeys, getValues)}

        # This for loops idea is to place empty spaces were player hasn't been yet (TRUE) and appends location on place player does (FALSE) switch deze
        land_name = []

        for place, first_entered in getKeysAndValues.items():
            if first_entered == True:
                land_name.append(place)
            else:
                land_name.append(' ' * len(place))

        usr_map = f'''
                                          -----------
                                         |           |
                         -----------     |           |
                        |           |  → | {land_name[9]} |
                        |           |     -----------
                        | {land_name[1]}  |
                         -----------
                            ↓    ↑
         -----------      -----------      -----------
        |           |  ← |           |  ← |           |
        |           |    |           |    |           |
        |{land_name[3]}| →  |   {land_name[2]}   | →  |{land_name[3]}|
         -----------      -----------      -----------
            ↓    ↑           ↓    ↑           ↓    ↑
         -----------      -----------      -----------
        |           |  ← |           |  ← |           |
        |           |    |           |    |           |
        |    {land_name[4]}   | →  |    {land_name[0]}   | →  |    {land_name[8]}   |
         -----------      -----------      -----------
            ↓    ↑                            ↓    ↑
        -----------      -----------      -----------
        |           |  ← |           |  ← |           |
        |           |    |           |    |           |
        |{land_name[5]}| →  |   {land_name[6]}   | →  |{land_name[7]}|
         -----------      -----------      -----------
        
        Press 'ENTER' to continue
        Press 'CTRL' to continue and clear the screen
        '''
        return(usr_map)

    @staticmethod
    def locator(location, first_entered):
        ''' Tracks if player has visited location before '''

        dic_locator = {
            'Home': False,
            'Wildland': False,
            'North': False,
            'North__West': False,
            'West': False,
            'South__West': False,
            'South': False,
            'South__East': False,
            'East': False,
            'DarkLands': False
        }

        # Changes value to True when player first enterd a location.
        if dic_locator[location] == False:
            dic_locator[location] = True

        return dic_locator