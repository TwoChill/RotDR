import player_location


def look(usrName, usrGendr, location):
    print("look menu")
    if location == 'garden':
        player_location.garden(usrName, usrGendr, location)
    elif location == 'Home':
        player_location.home(usrName, usrGendr, location)
    elif location == 'North':
        player_location.north(usrName, usrGendr, location)
    elif location == 'North_West':
        player_location.north_west(usrName, usrGendr, location)
    elif location == 'West':
        player_location.west(usrName, usrGendr, location)
    elif location == 'South_West':
        player_location.south_west(usrName, usrGendr, location)
    elif location == 'South':
        player_location.south(usrName, usrGendr, location)
    elif location == 'South_East':
        player_location.south_east(usrName, usrGendr, location)
    elif location == 'East':
        player_location.east(usrName, usrGendr, location)
    elif location == 'DarkLands':
        player_location.darklands(usrName, usrGendr, location)
    elif location == 'Wildland':
        player_location.wildlands(usrName, usrGendr, location)
    elif location == 'Tower':
        player_location.tower(usrName, usrGendr, location)


def dig(usrName, usrGendr, location):
    print('dig fucntion')
    # here should be a dict with every lil stuf that can be found on the floo
    # every land has a diffrent dict with value to use for shop shoptrader

    # def dig(location, quest1, quest2, quest3):
    # randomnr chooses wich item is RETURND with value
#     #  can dig anywhere to find something or certain lores
#     #  droprate of items depends on were you are in stroy
#     #  depending on location, items to find
#     #  there's a time delay for this action
#     # some books are only found throudigging
#     # dictonarie clasified by region cost as value
    print('dig function')


def spellbook():
    # menu of:
    # How to lift grandcloaking spellbook
    # How to make a invisable grandcloaking
    # wand, claok, t-stone ...
    # How to make a t-stone
    # other way to - dark invisable cloak - use ???
    # etc

    # def inventory():
    #     # usrname list of items with amout
    #     # this can be used to append to shoptrader and other quest dudes
    #     # so prorgram knows what to have and not
    print('Spellbook')
