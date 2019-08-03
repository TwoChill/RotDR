
import os


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

    while True:
        usr_command = enter_command(usrName, usrGendr, location, "start_menu")

        if usr_command == 'PLAY':
            os.system('clear')
            player_info(usrName, usrGendr, location)
        elif usr_command == 'HELP':
            help('start_menu')
        elif usr_command == 'QUIT':
            quit()
        else:
            print('\nI didn\'t get that!\n')


def enter_command(usrName, usrGendr, location, game_progression):

    usr_command = str(input(':> ').upper())

    if usr_command == 'LOOK':
        look(usrName, usrGendr, location)

    elif usr_command == 'DIG':
        dig(usrName, usrGendr, location)

    elif usr_command == 'MAP':
        map(usrName, usrGendr, location)

    elif usr_command == 'HELP':
        usr_command = help(game_progression)
        # return usrName, usrGendr, location, usr_command
    else:
        return usr_command


def player_info(usrName, usrGendr, location):

    print('''
You are about to embark on a journey of the imagination.
Full of everything your imagination can fill ...

.. With a helping hand offcourse ..


''')

    usrGendr = str(input("Will you be playing as a Boy or a Girl?\n:> ")).upper()

    if usrGendr == 'BOY':
        print('\nA Boy has been created!\n\n')
        usrGendr = usrGendr_boy
    elif usrGendr == 'GIRL':
        print('\nA Girl has been created!\n\n')
        usrGendr = usrGendr_girl
    else:
        randomnr = random.randint(1, 3)

        if randomnr == 1:
            usrGendr = 'BOY'
            print("\nI think I'll make a boy from clay.\n\n")
            usrGendr = usrGendr_boy
        else:
            usrGendr == 'GIRL'
            print("\nI think I'll make a girl from my rib.\n\n")
            usrGendr = usrGendr_girl

    usrName = str(input("Now choose your characters Name:\n:> ")).capitalize()

    while True:
        if " " in usrName:
            print('\nI just need one strong name...\n')
            usrName = str(
                input("\nChoose your characters name:\n:> ")).capitalize()
            continue
        elif usrName == "":
            print('\nI just need one strong name...\n')
            usrName = str(
                input("\nChoose your characters name:\n:> ")).capitalize()
            continue
        else:
            answer = str(
                input((f'\nIs "{usrName}" correct? (Y/N):\n:> ')).upper())
            if answer == "":
                continue
            elif (answer == 'Y') or (answer == 'YES'):
                tutorial_quest(usrName, usrGendr, location)
            elif (answer == 'N') or (answer == 'NO'):
                usrName = str(
                    input("\nChoose your characters name:\n:> ")).capitalize()
                continue
            else:
                continue
        break

    return usrName, usrGendr
