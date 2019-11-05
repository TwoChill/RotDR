import os
import time
import sys
import random
import keyboard  # pip install keyboard
import engine
import platform


usr_name_color = 'orange'
usr_answer = ('yes', 'y', 'no', 'n')
usrGendr_boy = ("he", "his", "him", "his",
                "He", "His", "Him", "His")
usrGendr_girl = ("she", "hers", "her", "her",
                 "She", "Hers", "Her", "Her")
mentorName = ''
mentorName_color = 'blue'

tspeed = 0.05
txt_wait = 3


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

                time.sleep(txt_wait)
                engine.sys_clear()

                usrGendr = usrGendr_boy
            elif usrGendr == 'girl':
                text = '\n\n\t\tA Girl has been created!\n\n'
                Typing(tspeed, text)

                time.sleep(txt_wait)
                engine.sys_clear()

                usrGendr = usrGendr_girl
            else:
                randomnr = random.randint(0, len(fAI_CC) - 1)
                Typing(tspeed, fAI_CC[randomnr])
                time.sleep(txt_wait)
                engine.sys_clear()

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
                time.sleep(txt_wait)
                engine.sys_clear()

                usrName = str(
                    input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                continue
            else:
                answer = str(
                    input((f'\n\t\tIs "{usrName}" correct? (Y/N):\n\t\t:> ')).lower())

                if '' == answer in usr_answer[2:]:

                    Typing(tspeed, fAI_CC[randomnr])
                    time.sleep(txt_wait)
                    engine.sys_clear()

                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
                elif answer in usr_answer[:2]:
                    engine.sys_clear()
                    text = '\n\n\t\t{} has been created!\n\n\tInitialization: Started\n\nInitialize in:\n3 ...\n2 .. \n1 . \n'

                    Typing(0.05, text.format(usrName))
                    time.sleep(txt_wait)

                    engine.matrix()
                else:
                    engine.sys_clear()
                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
            break

        self.usrName = Typing.text_decor(
            Typing.text_color(usrName, usr_name_color), 'bold')
        self.usrName_Plurar = usrName + "'s"
        self.usrGendr = usrGendr

        return [self.usrName, self.usrName_Plurar], self.usrGendr

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
        self.mentorName_Plurar = mentorName + "'s"

    def get_name(self, usrName, usrGendr):
        mentorName = str(
            input(
                f"\n\n{usrName} just woke up and rememberd {usrGendr[3]} mentor's name..\n:> "))

        while True:
            if mentorName == '':
                text = f"\nIt's been a rough nap... what was {usrName}'s mentor's name?'\n"
                Typing(tspeed, text)

                mentorName = str(
                    input("\n:> ")).capitalize()
                continue
            else:
                answer = str(
                    input((f'\n"{mentorName}"? That sounds about right.. (Y/N):\n:> ')).lower())
                if answer == "":
                    continue
                elif answer.lower() in usr_answer[:2]:
                    break
                else:
                    mentorName = str(
                        input("\nChoose your mentor's name:\n:> ")).capitalize()
                    continue
            break
        self.usrName = Typing.text_decor(
            Typing.text_color(usrName, usr_name_color), 'bold')
        self.usrName_Plurar = usrName + "'s"
        self.mentorName = Typing.text_decor(
            Typing.text_color(mentorName, mentorName_color), 'bold')
        self.mentorName_Plurar = mentorName + "'s"

        return [self.mentorName, self.mentorName_Plurar]


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
            engine.sys_clear()

            text = '''
            You are about to embark on a journey of the imagination.
                Full of everything your imagination can fill

                    .. With a helping  hand offcourse ..

                   .... So let's create a character! ....'''
            Typing(0.05, text)
            time.sleep(txt_wait)
            engine.sys_clear()


class Menus(object):
    def __init__(self, location):
        self.location = location
        self.game_name = engine.game_name()

    def start_menu(self, location):
        engine.sys_clear()
        print(self.game_name)
        tspeed = 0.005

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
        engine.enter_command(location)

    def get_help(self, location):

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

                      - Press "CTRL" to speed up txt -
                        - Good luck and have fun!! -
                        ############################
        '''
        if location == 'Beginning':
            engine.sys_clear()
            print(self.game_name)
            tspeed = 0.005
            Typing(tspeed, Help_Menu)
            engine.enter_command(location)
        else:
            Typing(tspeed, Help_Menu)
            engine.enter_command(location)


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
    def text_color(cls, text, color):
        ''' This function color's text '''

        if color == 'red':
            return bcolors.FAIL + text + bcolors.ENDC
        elif color == 'green':
            return bcolors.OKGREEN + text + bcolors.ENDC
        elif color == 'blue':
            return bcolors.OKBLUE + text + bcolors.ENDC
        elif color == 'orange':
            return bcolors.WARNING + text + bcolors.ENDC

    @classmethod
    def text_decor(cls, text, decor):
        ''' This function decorates text like UNDERLINe and BOLD '''

        if decor == 'underline':
            return bcolors.UNDERLINE + text + bcolors.ENDC
        elif decor == 'bold':
            return bcolors.BOLD + text + bcolors.ENDC


class Quest(Hero):

    def __init__(self, usrName, usrGendr, location):
        super().__init__(usrName, usrGendr, location)

    def tutorial_quest(self, usrName, usrGendr, location):
        time.sleep(txt_wait)

        mentorName = ''
        mentorName_Plurar = ''

        text = f'''
{usrName} slowly opens {usrGendr[3]} eyes from {usrGendr[3]} hammock.

The first thing {usrName} notice
is the warm sun on {usrGendr[3]} face,
birds chirping faintly in the background,
and a lukewarm breeze,
that carries a sweet scent of primrose roses.

Peacefull..


Afther a few moments,
{usrName} hears the sound of a door opening.
{usrGendr[4]} looks up and sees {usrGendr[3]} mentor standing in a doorway.
'''
        Typing(tspeed, text)

        engine.obtains('LOOK', usrName)
        engine.cmd_tutorial('look')

        input(bcolors.FAIL + '\n:> ' + bcolors.ENDC)
        engine.sys_clear()

        text = f'''
{usrName} looks around at the {location}
and sees a big tree inside a grass field
surrounded by a man-made wooden fence.

There's a wooden chop-block at the end of the grassfield
next to a stands sturdy man-made wooden log.

A feeling of familiarity came over {usrName} as {usrGendr[0]} sees
{usrGendr[3]} mentor standing in the doorway of the log.
'''
        Typing(tspeed, text)
        time.sleep(txt_wait)

        mentor = Mentor(mentorName, mentorName_Plurar)
        mentorName = mentor.get_name(usrName, usrGendr)
        engine.sys_clear()

        text = f'''
With a confused face, {mentorName[0]} walks up to {usrName}
and he asks to help him find a map that he burried
somewhere around this {location}.

You decide to help {mentorName}.
He places his hand on {usrName}'s forehead,
while mumbling some kind of strange mantra.

While listning to the mantra, {usrName} can't help but notice,
a strang thermic force comming of {mentorName} body.

Suddenly {mentorName[1]} hand glows
and a rainbow-colored thermic force shoots out of his hand ...


A warm feeling came over {usrName}.
'''
        Typing(tspeed, text)

        engine.obtains('DIG', usrName)
        engine.cmd_tutorial('dig')

        input(bcolors.FAIL + '\n:> ' + bcolors.ENDC)
        engine.sys_clear()

        text = f'''
{mentorName} pukes from excaustion!
But he looks happy...
Probably beacuse you can help find his map now.\n'''
        Typing(tspeed, text)
        time.sleep(txt_wait)

        text1 = f'''
{usrName} puts {usrGendr[3]} hand on the ground..
The same rainbow-colored thermic force
shoots from {usrGendr[3]} arm through and out off his hand!\n'''
        Typing(tspeed, text1)
        time.sleep(txt_wait)

        text2 = f'''
{usrName} somehow opens a small black portal
with evaporating 1's and 0's around the edges.\n'''
        Typing(tspeed, text2)

        text3 = f'''
{usrName}'s hand went through the ground's dimension and {usrGendr[0]} felt something...\n'''
        Typing(tspeed, text3)
        time.sleep(txt_wait)

        text4 = f'''
It was the map {mentorName} was looking for!'''
        Typing(tspeed, text4)
        time.sleep(txt_wait)
        engine.sys_clear()

        text5 = f'''
{usrName} turns around and gives the map to {usrGendr[3]} mentor.

With relieve {mentorName} looks at the map
and with a snap of his fingers the map vanishes .. !?!

{mentorName} looks at {usrName} and asks {usrGendr[3]} to use the map ..
'''
        Typing(tspeed, text5)

        engine.obtains('MAP', usrName)
        engine.cmd_tutorial('map')

        input(bcolors.FAIL + '\n:> ' + bcolors.ENDC)

        first_entered = ''
        map = Map(usrName, usrGendr, location)
        map.get_map(usrName, usrGendr, location, first_entered)

        input()

        engine.comming_soon()

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
        self.first_entered = True

        # Create new instance to separate keys en values of dict in static 'locator' methode
        map = Map(usrName, usrGendr, location)

        # Checks to see if player location is True or False.
        # Returns dictionary with locations as key and True as values (where player has visited.)
        check = map.locator(location, first_entered)

        # This block creates a new dictionary with boolean values ​​corresponding with visited places by placer.
        getkeys = map.locator(location, first_entered).keys()
        getvalues = map.locator(location, first_entered).values()
        getkeys_getvalues_zip = {key: value for key,
                                 value in zip(getkeys, getvalues)}

        # This for loops idea is to place empty spaces were player hasn't been yet (TRUE) and appends location on place player does (FALSE) switch deze
        land_name = []

        for place, first_entered in getkeys_getvalues_zip.items():
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
        print(usr_map)

    @staticmethod
    def locator(location, first_entered):

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

        # This block checks players location. If it's player first visit, changes the dict value to True
        if dic_locator[location] == False:
            dic_locator[location] = True

        return dic_locator
