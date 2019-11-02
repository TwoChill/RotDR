import os
import time
import sys
import random
import keyboard  # pip install keyboard
import engine
import platform


usr_answer = ('yes', 'y', 'no', 'n')
usrGendr_boy = ("he", "his", "him", "his",
                "He", "His", "Him", "His")
usrGendr_girl = ("she", "hers", "her", "her",
                 "She", "Hers", "Her", "Her")
mentorName = ''

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
        # super().__init__(hp, mp, atk, df, magic)
        self.usrName = ''
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

                time.sleep(3)
                engine.sys_clear()

                usrGendr = usrGendr_boy
            elif usrGendr == 'girl':
                text = '\n\n\t\tA Girl has been created!\n\n'
                Typing(tspeed, text)

                time.sleep(3)
                engine.sys_clear()

                usrGendr = usrGendr_girl
            else:
                randomnr = random.randint(0, len(fAI_CC) - 1)
                Typing(tspeed, fAI_CC[randomnr])
                time.sleep(3)
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
                time.sleep(3)
                engine.sys_clear()

                usrName = str(
                    input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                continue
            else:
                answer = str(
                    input((f'\n\t\tIs "{usrName}" correct? (Y/N):\n\t\t:> ')).lower())

                if '' == answer in usr_answer[2:]:

                    Typing(tspeed, fAI_CC[randomnr])
                    time.sleep(3)
                    engine.sys_clear()

                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
                elif answer in usr_answer[:2]:
                    engine.sys_clear()
                    text = '\n\n\t\t{} has been created!\n\n\tInitialization: Started\n\nInitialize in:\n3 ...\n2 .. \n1 . \n'

                    Typing(0.05, text.format(usrName))
                    time.sleep(1)

                    engine.matrix()
                else:
                    engine.sys_clear()
                    usrName = str(
                        input("\n\t\tChoose your characters Name:\n\t\t:> ")).capitalize()
                    continue
            break

        self.usrName = usrName
        self.usrGendr = usrGendr

        return usrGendr

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

        self.mentorName = mentorName

        return mentorName


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
            time.sleep(3)
            engine.sys_clear()

    def get_map(self, location):
        '''Show map and current location'''
        pass


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

        if location == 'Beginning':
            engine.sys_clear()
            print(self.game_name)
            tspeed = 0.005

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

            if keyboard.is_pressed('ctrl'):
                time.sleep(0.01)
                speed = 0.00001

            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(speed)

        sys.stdout.write('\n')
        sys.stdout.flush()

    # create a option to press ENTER and skip the rolling text #


class Quest(Hero):

    def __init__(self, usrName, usrGendr, location):
        super().__init__(usrName, usrGendr, location)

    def tutorial(self, usrName, usrGendr, location):

        mentorName = ''

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

        time.sleep(2)

        text = bcolors.FAIL + bcolors.BOLD + bcolors.UNDERLINE + \
            "\n# Tutorial: Use command 'LOOK' #" + bcolors.ENDC
        text1 = bcolors.WARNING + bcolors.UNDERLINE + \
            "\nType" + bcolors.FAIL + " 'look' " + \
            bcolors.WARNING + "to look around your surroundings" + bcolors.ENDC

        Typing(tspeed, [text, text1])

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
        time.sleep(3)

        mentor = Mentor(mentorName)
        mentorName = mentor.get_name(usrName, usrGendr)

        time.sleep(3)
        engine.sys_clear()

        text = f'''
With a confuced face, {mentorName} walks up to {usrName}
and he asks to help him find a map that he burried
somewhere around this {location}.

You decide to help {mentorName}.
He places his hand on {usrName}'s forehead,
while mumbling some kind of strange mantra.

While listning to the mantra, {usrName} can't help but notice,
a strang thermic force comming of {mentorName} body.

Suddenly {mentorName}'s hand glows
and a rainbow-colored thermic force shoots out of his hand ...


A warm feeling came over {usrName}.
'''
        Typing(tspeed, text)
        time.sleep(4)

        engine.obtains('DIG', usrName)
        engine.cmd_tutorial('dig')
        time.sleep(3)

        text = f'''
{mentorName} pukes from excaustion!
But he looks happy...
Probably beacuse you can help find his map now.\n'''
        Typing(tspeed, text)
        time.sleep(2)

        text1 = f'''
{usrName} puts {usrGendr[3]} hand on the ground..
The same rainbow-colored thermic force
shoots from {usrGendr[3]} arm through and out off his hand!\n'''
        Typing(tspeed, text1)
        time.sleep(1)

        text2 = f'''
{usrName} somehow opens a small black portal
with evaporating 1's and 0's around the edges.\n'''
        Typing(tspeed, text2)

        text3 = f'''
{usrName}'s hand went through the ground's dimension and {usrGendr[0]} felt something...\n'''
        Typing(tspeed, text3)
        time.sleep(3)

        text4 = f'''
It was the map {mentorName} was looking for!'''
        Typing(tspeed, text4)
        time.sleep(4)
        engine.sys_clear()

        text5 = f'''
{usrName} turns around and gives the map to {usrGendr[3]} mentor.

With relieve {mentorName} looks at the map
and with a snap of his fingers the map vanishes .. !?!

{mentorName} looks at {usrName} and asks {usrGendr[3]} to use the map ..
'''
        Typing(tspeed, text5)
        time.sleep(3)

        engine.obtains('MAP', usrName)
        engine.cmd_tutorial('map')

        answer = input(bcolors.FAIL + '\n:> ' + bcolors.ENDC)
        
        first_entered = True

        while True:
            if answer == 'map':
                map = Map(usrName, usrGendr, location)
                map.get_map(usrName, usrGendr, location, first_entered)
            else:
                answer = input(bcolors.FAIL + '\n:> ' + bcolors.ENDC)

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
        self.location = location
        self.first_entered = first_entered

        # Create new instance to separate keys en values of dict in static 'locator' methode
        map = Map(usrName, usrGendr, location)
        x = map.locator(location, first_entered).keys()
        y = map.locator(location, first_entered).values()
        
        # Every time get_map is called, this block creates a new dictionary with boolean values ​​corresponding with visited places by placer.
        land_name_zip = {key: value for key, value in zip(x, y)} 
        
        land_name = []
        for place in land_name_zip.keys():       
            if land_name_zip.values() is not True:
                land_name.append(place)
            else:
                land_name.append('' * len(place))


        mapz = f'''
    {usrName} opens {usrGendr[3]} map! (in {location})
                                          -----------
                                         |           |
                         -----------     |           |
                        |           |  → | {land_name[9]} |
                        |           |     -----------
                        | {land_name[1]} |
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
        '''
        return mapz

    @staticmethod
    def locator(location, first_entered):

        dic_locator = {
            'Home': True,
            'Wildland': True,
            'North': True,
            'North__West': True,
            'West': True,
            'South__West': True,
            'South': True,
            'South__East': True,
            'East': True,
            'DarkLands': True
        }
        
        # Change the value to False then shows up in the map.
        if first_entered is True:
            dic_locator[location] = False

        return dic_locator