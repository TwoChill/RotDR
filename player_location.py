false = False


def land_map(usrName, usrGendr, location, bool):
    land_name = []          # Makes the map look empty..
    # ..except by conditions below
    if ((location == 'Home' or location == 'Garden') and (first_entered(location, bool) == True)):
        land_name = ['     ', '           ', '    ', '           ', '     ',
                     '           ', '    ', '         ', '         ', '     ', 'HOME']
    # Displays same map if player goes to Garden more the once but hasn't been to other areas.
    elif ((location == 'Home' or location == 'Garden') and (first_entered(location, bool) == false)):
        #        print('>>> bool is false =', bool)
        land_name = ['     ', '           ', '    ', '           ', '     ',
                     '           ', '    ', '         ', '         ', '     ', 'HOME']

    map = f'''
{usrName} opens {usrGendr[3]} map! (in {location})
                                       -----------
                                      |           |
                      -----------     |           |
                     |           |  → |   {land_name[9]}   |
                     |           |     -----------
                     |   {land_name[0]}   |
                      -----------
                        ↓    ↑
     -----------      -----------      -----------
    |           |  ← |           |  ← |           |
    |           |    |           |    |           |
    |{land_name[1]}| →  | {land_name[7]} | →  | {land_name[8]} |
     -----------      -----------      -----------
       ↓    ↑           ↓    ↑           ↓    ↑
     -----------      -----------      -----------
    |           |  ← |           |  ← |           |
    |           |    |           |    |           |
    |    {land_name[2]}   | →  |    {land_name[10]}   | →  |    {land_name[6]}   |
     -----------      -----------      -----------
       ↓    ↑                            ↓    ↑
     -----------      -----------      -----------
    |           |  ← |           |  ← |           |
    |           |    |           |    |           |
    |{land_name[3]}| →  |   {land_name[4]}   | →  |{land_name[5]}|
     -----------      -----------      -----------
    '''

    print(map)
    input('Press ENTER to close the map :> ')
    print(f'\n\n{usrName} closes {usrGendr[3]} map!\n\n')


def first_entered(location, bool):

    dic_first_entered = {
        'Home': True,
        'Garden': True,
        'usrName_room': True,
        'Wildland': True,
        'North': True,
        'North_West': True,
        'West': True,
        'South_West': True,
        'South': True,
        'South_East': True,
        'East': True,
        'DarkLands': True,
    }
    # Change the value of a location to false
    if bool is False:
        dic_first_entered[location] = False

    # Returns the value of a location.
    return dic_first_entered.get(location)


def garden(usrName, usrGendr, location):
    print('garden')


def home(usrName, usrGendr, location):

    # f statement little first entered afther standard intro
    # print('Home They Are')
    # location = 'Home'
    # Your home
    # Your mentor
    # Your room with Lore read    functie
    print('home')

# def usrName_room(location):
#     location = 'usrName_room'
#     # here are some books with lore
#     # rest (saves the game)
#
# def wildlands(location):
#     location = 'Wildland'
#
#
# def north(location):
#     location = 'North'
#
# def north_west(location):
#     location = 'North_West'
#
# def west(location):
#     location = 'West'
#
# def south_west(location):
#     location = 'South_West'
#
# def south(location):
#     location = 'South'
#
# def south_east(location):
#     location = 'South_East'
#
# def east(location):
#     location = 'East'
#
# def dark_lands(location):
#     location = 'DarkLands'
