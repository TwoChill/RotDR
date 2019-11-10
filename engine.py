import os
import time
import sys
import random
import base as clss

import platform

txtSpeed = 0.05
txtWait = 0
usrNameColor = None
mentorNameColor = None

usrGendr_Boy = ("he", "his", "him", "his",
                "He", "His", "Him", "His")
usrGendr_Girl = ("she", "hers", "her", "her",
                 "She", "Hers", "Her", "Her")

usrAnswer = ('yes', 'y', 'no', 'n')

# This fAI (fake AI) list are responses given when the user types an unknow command. (Can be expanded upon.)
fAI = ['Uhmm.. I think you misspelled..', "'{}', is kinda.. forein to me.",
       "Nope, I didn't get that!", '.......... -_-',
       'We all have brainfarts sometimes ....', "I don't think '{}' is the answer..",
       'Oeps, brainfart! Again please!', "That's just not correct.",
       "I'm sorry, but I don't know what '{}' means.", "That's what she! said.",
       ".. 'help' could be usefull .."]


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")


def comming_soon():
    ''' Displays 'COMMING SOON' message. Meaning the rest of the game hasn't been programmed yet '''

    time.sleep(txtWait)
    print('\n\t\t\t!! COMMING SOON !!\n')
    time.sleep(txtWait)
    quit()


def cmd_tutorial(cmd):
    ''' Prints out an explanation on how to use commands '''
    text = clss.bcolors.FAIL + clss.bcolors.BOLD + clss.bcolors.UNDERLINE + \
        "\n# Tutorial: Use command '" + cmd.upper() + "' #" + clss.bcolors.ENDC

    if cmd == 'look':
        text1 = clss.bcolors.WARNING + clss.bcolors.UNDERLINE + \
            "\nType" + clss.bcolors.FAIL + " '" + cmd + "' " + \
            clss.bcolors.WARNING + "to look around your surroundings.\n" + clss.bcolors.ENDC

    if cmd == 'map':
        text1 = clss.bcolors.WARNING + clss.bcolors.UNDERLINE + \
            "\nType" + clss.bcolors.FAIL + " '" + cmd + "' " + \
            clss.bcolors.WARNING + "to see were you are.\n" + clss.bcolors.ENDC

    if cmd == 'dig':
        text1 = clss.bcolors.WARNING + clss.bcolors.UNDERLINE + \
            "\nType" + clss.bcolors.FAIL + " '" + cmd + "' " + \
            clss.bcolors.WARNING + "to open a small black portal.\n" + clss.bcolors.ENDC

    clss.Typing(txtSpeed, [text, text1])

    input(clss.bcolors.FAIL + '\n:> ' + clss.bcolors.ENDC)


def obtains(cmd, usrName):
    ''' When HERO obtains something, a text will be displayed '''
    print(usrName)
    time.sleep(txtWait)
    clss.Typing(txtSpeed, clss.Typing.text_decor(
        'red', ['bold', 'underline'], f'\n\t{usrName} OBTAINS {cmd}!\n'))
    time.sleep(txtWait)


def enter_command(location):
    ''' Function is used to enter command into the game '''
    usr_command = str(input('\t\t\t\t\t\t:> ')).lower()

    if location == 'Beginning':

        if usr_command in ('play', 'Play', 'PLAY'):
            Start_Game = clss.Location(location)
            Start_Game.get_intro(location)

        elif usr_command in ('help', 'Help', 'HELP'):
            Help = clss.Menus(location)
            Help.get_help(location)

        elif usr_command in ('load', 'Load', 'LOAD'):
            comming_soon()

        elif usr_command in ('back', 'Back', 'BACK'):
            Restart_Game = clss.Menus(location)
            Restart_Game.start_menu(location)

        elif usr_command in ('quit', 'Quit', 'QUIT'):
            quit()
        else:
            usr_type_error(location, usr_command)
    else:
        if usr_command == 'look' and location != 'Beginning':
            # Class Locations. Per location 1. Intro
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'dig' and location != 'Beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'map' and location != 'Beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'spellbook' and location != 'Beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'save' and location != 'Beginning':
            print(f'\t\t\t{usr_command} command is COMMING SOON').upper()
            comming_soon()

        elif usr_command == 'load' and location != 'Beginning':
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
    if location == 'Beginning':
        print('\t\t\t' + fAI[randomnr].format(usr_command) + '\n')
        enter_command(location)
    else:
        print(fAI[randomnr].format(usr_command) + '\n')
        enter_command(location)


def game_name():
    ''' The gamename in TextART form. '''

    game_name = '''
8888888b.  d8b                                                                                                          
888   Y88b Y8P                                                                                                          
888    888                                                                                                              
888   d88P 888 .d8888b   .d88b.                                                                                         
8888888P"  888 88K      d8P  Y8b          .d888       888    888                                                          
888 T88b   888 "Y8888b. 88888888         d88P"        888    888                                                          
888  T88b  888      X88 Y8b.             888          888    888                                                          
888   T88b 888  88888P'  "Y8888  .d88b.  888888       888888 88888b.   .d88b.                                             
                                d88""88b 888          888    888 "88b d8P  Y8b                                            
                                888  888 888          888    888  888 88888888                  
                  8888888b.     Y88..88P 888          Y88b.  888  888 Y8b.     8888888b.  d8b      888           
                  888  "Y88b     "Y88P"  888           "Y888 888  888  "Y8888  888   Y88b Y8P      888              
                  888    888                                                   888    888          888
                  888    888 888d888  8888b.   .d88b.   .d88b.  88888b.        888   d88P 888  .d88888  .d88b.  888d888 
                  888    888 888P"       "88b d88P"88b d88""88b 888 "88b       8888888P"  888 d88" 888 d8P  Y8b 888P"   
                  888    888 888     .d888888 888  888 888  888 888  888       888 T88b   888 888  888 88888888 888     
                  888  .d88P 888     888  888 Y88b 888 Y88..88P 888  888       888  T88b  888 Y88b 888 Y8b.     888     
                  8888888P"  888     "Y888888  "Y88888  "Y88P"  888  888       888   T88b 888  "Y88888  "Y8888  888     
                                                   888                                                                  
                                              Y8b d88P                                                                  
                                               "Y88P"                                                                   


                                               '''
    sys_clear()

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
    clss.Typing(txtSpeed, space)
    sys_clear()

    return None


def quit():
    ''' Exits the game with the game logo '''

    sys_clear()

    text = '''
`+++++/////+++++osyhdmdhyysyhhhddmmmmNNmds+s+ymmmmmmmmmmmmmmmNmo.                                                                                       
                       `++///+++osyhdmdhyso+/++++++++++oohdmmmmmmso+ohmmmmNmmmmmmmmNh/`                            `--.`      :+-`                                             
                      `:/+osyddmdhso/:://///++++++++++++++oydmmmmmds++hmNNmmmmmmmmNh:`                    `-..`   `/dNmmds+/:smmmmy:`  `-.                                     
                     :shddhyo+/:://///////////+++++++++++++++ydmmmmmho/sdmmmmmmmNNy:`                     :mNmmhyssmNNmNNNNmNNNNNNmmdhhdmmy:`                                  
                  `/sso/:////+/////////////++++++++++++++++++++ymmmmmmy+/smNNNNMMs:`           ./ssso++/:omNNNNNNNmNmmmmmmmmmmmmmmmmmmmNNNmmh:` `..                            
                -//.``....--::////:::-::::::::::::::::://+++++++ohmmmmmds/:odNMMy:`            `oNmmmNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNmmdmmmy`                          
               `.`             ````` `` `````...--:://++++++++++++ymmmmmmho+//ss:`       -o++/ohNNMMMMNNNmmmmmmmmmmmmmmmmdmddddhhdddddmmmmmmmmmmmmmmy.`                        
                                       `..--::///++++++++++++++++++odmmmmmdyoo+/:-.`` ./sdNNNNMMMMMNNNmmmmmdmmmmmmmdddhyssooooo+oooossyyyhddmmmmmmmNNdm/                       
                                        `.:/++++++///////////////+++odmmdmmdhsooo++//:+ydmNNMMMMMMMNNmmmmmmmmmmmdhyso++++++++++++++++++++ooosyhddmmmmNNN+``yho+`               
                                          ``-::::::-------..--://++++ohmmmmmmds++++ooo++++ooossyyyyyyhdmmmmmmddyo/////++++////////////////++++oosyhdmmmNm+.mdhs-               
`.--::::--.`                                  `````````  `.--://++++++ommmmmmmdho+////+oo+++++++++++oosyhdmdho+//++++++//++osoo+++++++++++///+++++osyhdmmmhdmo-                
mNNNNNNNNNmmdyo:.                                    ```.--:://+++++++ommmmmmmmdyso++/////////////+++++++ooo:/+sssoo+//+ossoo+/////+++++++ooossooo+++osydmmNdo-                
MMMMMMMMMMMMMMMNNds/`                               `.-:://++++++++++ohmmmmmmmmmdhyyyyyyyssssssss+++++++++/::yhhso+//+oo+/:-.``````.--:/+oshdmmdddddhyyssshNdo/`               
MNNNNmmmNNNNNNNNNNNNmo.                               `-/++++++++++oydmmmmmmmmNNNmmmmmmmmmmdddddhdsoo++///+::dho+////:-.``             ``-/oydmmNNNNMNNNmddNdo+:`              
mmmmmddhddNNmNNmmNmmNmd+`                               `:+++++osyddmmmmmmmmmNNNMMMMNNmmmmdyhsssos++++++/://:yo+/:.``                     `-/odmNMMMMMMMNNmhh++oo.             
dhhy:.```.-.-/oymNmmmmmmo`                         `-/shdmmhhhdmmmmmmmmmmmNNMMMMMMMNmmmmmmysso++++++//:++::-:+:.`                           `/ohNNNmmmmmmdyo+++shh-            
:.``           `.+dNmmmmm+                         .sMMMMMMNmmmmmmmmmmmNNNMMMMMMMNNmmmmmdhoo+++++++++:./+/:````                              `/omddhhyyyhs++odo/+yd:           
                  .sMmmmmy`                       .:yMMMMMMMNNmmmmmmmmmmNNNMMMMMMNmmmmmmhsoo+++++o+++/.so+:`                                  -odyssso+o++++smmd/+hh           
                   `dNmmmy`                   .:+ydNNMNNNmmNmmmmmmmmmmmmmmNMMMMMMNmmmmmdssyyysysoo+++/-yo+.                                   `oso+++++++/+/+yshd/yd           
                    sMNmmo`                  ./mNNMNNNmmmmmmmmmmmmmmmmmmmmNMMMMMMNmmmmmdhdddyso++++++-/o/-                                     .:+++++++///++++omshh           
                    hMNmd/                  `-sNMMNNNmmmmmmmmmmmmmmmmmmmmmNMMMMNNNmmmmmdmdmho++++++/--+/.`                                      ``-/so+/////ss/odmNo           
                 ://NNmms.               `:odNMMMNNmmmmmmmmmmmmmmmmmmmmmmmNMMNmmmmmmmmmmmdho++++++/..:-`                                           /Ns:///o+/ys+ohms           
                `mNNMmmy-              `:ymNMMMNNmmmmmmmmmmmmmmmmmmmmmmmmmNMNmmmmmmmmmmddho+++++/-..`                                       `:shy+-/mo:.://o//so++yd-          
               `sMMMNdy:               ./dMMMMNmmmmmmmmmmmmmmmmmmmmmmmmmmmNNmmmmmmmmmmhsso+++:-.`.+-                                        /NMMNdshh-` `-+++:+o+/+yy`         
               +NMNmds+:`           `:ymMMMMMNmmmmmmmmmmmdmmmmmmmmmmmmmmmNNmmmmmmmmmdyo++++++/-`-o+`                                       :hMmMmyym/     -+++:++++/y/         
              +NNNdyo/:-`         `:ymNMMMMMNmmmmmmmmmmmdyhmmmddddmmmmmNNNmmmmmNmmNmhs+++++//-./s+-`                                     `-dMNdmysmy`      ./+//++h/+s`        
            `oNNho/..`            -smMMMMNNNmmmmmmmmmmmmmdhdmmmmmmdmmmmNNmmmmmddhmNmho++///--/yhs+/:`                                   .hNMMmdyydo.        -/+++++++/`        
           .ods:.`            `.:sdMMMMNNmmmmmmmmmmmmmmmmmdhmmmmmmmmmmmNMNmmmmmdhsydho+//+oymNmdyo+/:.                                  yMMMNhym+-:/:.       .-:/+//-`         
          `+/.               .odmNMMMMMNmmmmmmmmmmmmmmmmmmmmddmmmmmmmmNNMMNNmmmmhso++++/smMMMNmdho+o+/.                                 hMNmdy+h-hNds+`         `-.`           
                             `.hNMMMMMNNmmmmmmmmmmmmmmmmmmmmmdddmmmmmmmmmNMMNmmmmhs+++/-`-sNMMNmdyoydyo-`                               yMNdhsshydhyhh:                        
                           `-+hMMMMMMMMNmmmmmmmmmmmmmmmmmddmmmdydmdddhhyshNNmmmNmmdhssso+:.:ymMMNmhydmdy/`                              sMMNy+ss+ooshs:                        
                        `-+hmMMMMMMMNNMNmmmmmmmmmmmmmmmmmdhddmmdsdhyyssoooyNmmmmNNmmdsosys+-`-+hmNNmmNNmdy:`                            :NMNdyhmmNMNdh/  ````                  
                        -+mNMMMMMMMMNmNNmmmmmmmmmmmmmmmmmmmhhdmmhossoo++///hNmmmmmmmmdyo+os+:` `-odNNNMNNmmho-`       ``                `yNMNmmNMMMmdy+syhhhs/`                
                       `:yMMMMMMMMMMNmmmmmmmmmmmmmmmmmmddmmmdhddmo/++/::+ymMMMddmmmmmmdhs++/+/`   `-/ydNMMNNMNdyssssssyy+--`             `/NMMMmNMMMmy/hMMMNds.                
                   `/oydNMMMMMMMMMMMNmmmmmmmmmmmmmmmmmmdhhdmmdhhmh-/+ohmMMMMNy.-ohdmmmmdyo+/+/-`      `-+dNMMMMMMMMMMMMNmyhh.             `sMMMMNMMMNdooMMMMmo`                
.   ``      ```   `:dNMMNNNNMMMMMMMMMNmmmmmmmmmmmmmmmmmmmdyydmdddd+yMMMMMMMNs`   `-+sdmmmmhsso+/-`       .+dMMMNmmNMMMMMNmsms`             oMMMMMMMMNds+dMMNho                 
hs+/+y+-.../hhhsooymNNNNmmmmmNNMMMMMMMNmmmmmmmmmmmmmmmmmmmdhyhdddyooMMMMMMm/`        `-sdmNNmmddhs/:-:/oyhmmNNNmo++hNMMMMMhyh`      ``-:::omMMMMMMMMmhyoosdms-                 
mmmmmmmmmdmmNmmNNNNmmmmmmmmmmmmNNNNMMMNNmmmmmmmmmmmmmmmmmmmmdyyydho:NMMMMm-             `/yNMMMMMMMMNMMMMNNmmmmNd+/:dMMMMMdNhy-````/hmNNNMMMMMMMNNNNMMMNysmho`                 
mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdddmmmmmmmmmmmmmmmmmmmmmmmdhoydo-mMMNy.                 -smMMMMMMMMMMMNNmdydhMmyyyMMMMMMMNMNmmmdNMMMMMMMMNNNNNMMMMMMM+hNy/`                 
mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddhyyysssoshmNNNNNNNNmmmNNNmmmmmmyoyo-yNm/`                    .+hmNMMMMMMMMMMMddyNMMmNMMMMMMMMMMMMMMMMMMMNNmmNNNNmmmmNNMMmmms.                  
mmmmmmmmmmmmmmmmmmmmmmmmmmmddhyssoo+++++++ohNNNmmmmmmmmmmmNNmmmmo+o::s.              -os`     `./yNMMMMMMMMMMMNmNMMMMMMMNNNNmmmNNMMMMNmmdddddddhhhhhhhmMMMms.                  
mmmmmmmmmmmmmmmmmddddddddhyyssoo+++++/++ohmNNmmmmmdhhhddmmmmmmdds+o+-`             `sNMm.  .+hmNMMMMMMMMMMMMMMNNNNmmmmddddddddNNNMNmddddddddhhddhhhhhhh+sddh/`                 
mmmmmmmmmmmmmmddhysssssooo+++/////+++sydNNmmddhysso++++oshdmmmdhyos+/`.`          :dMMNs`.yNMMMMMMMMMMNNNmmmmmmmdddddddmmmmmNNNNNNmmmmmddddhhddhdhhhhy:  `-+s/`                
mmmmmmmmmmmmdhsso++++++++++++ooyhhdmmNmmmmmdhysoo++////+shdmmmdyyoo+/.dms:`    ``oNMMmddsdMMMMMMNNmmdddddddddddddmmNNMMNNNNNNmmmmddmmmmddddddddddhhhh/      `.`                
dddddddddhyysoo++++++++++ydmmNNNMMNNmmmmmmmmddhhyyyssyydmNNmmmmdyo+/-:NMMMmyo+yhmMMMmmdNMNNmmmmddddmmmmmmmddmmNNNMMNNNNNNmdddddddddddddddddddhhddmmhy-                         
ssssooooooo+++++++++++++sNmmmmdddmNMMMNNmmmmmmmmmmmmmmmmmmmmmmmhso+:-sNMMMMMMMMMMMNNmmmddddddddmmmmmmmmmNNNNMMMMMMMMNNmddddddddmddhhhhdddhhdmmmmdhy+                           
+++++++++++++++///::-...oMNmmdhs++oymMNNdddhhhhhhhhhyysoo++//+ossyhdNMMMMMMMMNNmmmmmmmmmNNNNNNMMMMMMMNNMMMMMMMMMNNmddddddmmmmdhhdmmmmmmdmmmmdddddds                            
`..---------....``      -mNNmdds+++++/.``               `.:oydNMMMMMMMMMMMMNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmddmNNNNNNNNNNNmmddddhhddddddddh:                            
                         -sdmmmmyooo/:.`            ./shmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhhhhhddmdhddmmmmdo`                            
                           `:yNmmdyss+/-`          .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMNNmddddhhdddddddmNNMNmddyys/`                             

                                                               
                                                               Thank you for playing!                                                               
                                                               '''

    clss.Typing(0.0009, [text, game_name()])

    sys.exit()
