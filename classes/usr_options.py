from functions import gf  # Game Functions

# Enter_Command maby should be a function instead of a class
# Enter_Command maby should be moved to gf (Game Function) file for.


class Enter_command(object):
    def __init__(self, location):
        self.location = location

        usr_command = str(input(':> ')).lower()

        if usr_command == 'play' and location == 'beginning':
            gf.clear()      # os.system('clear')
            gf.player_info(location)
        elif usr_command == 'help':
            print('!TO BE CONTINUED!')
            quit()
        elif usr_command == 'quit':
            print('Thank you for trying!\n!TO BE CONTINUED!')
            quit()
        else:
            print('\nI didn\'t get that!\n')


class Dig:

    def __init__(self, usrName, usrGendr, location):
        self.usrName = usrName
        self.usrGendr = usrGendr
        self.location = location
        print('Dig Fucntionn')


class Look:
    def __init__(self, usrName, usrGendr, location):
        self.usrName = usrName
        self.usrGendr = usrGendr
        self.location = location
