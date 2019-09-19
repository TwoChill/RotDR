# Change to from classes import <<whole file>> // menu or characters
from functions import gf  # Game Functions

from classes.menus import Start
from classes.usr_options import Enter_command

gf.clear()

location = 'beginning'

print('\n############################')
print('# Rise of the Dragon Rider #')
print('############################\n')
print('          - Play -          ')
print('          - Help -          ')
print('          - Quit -          ')
print('\n          Made by:          ')
print('       M.L. de France       ')
print('\n############################\n')

Enter_command(location)
