def look(usrName, usrGendr, location):
    print("look menu")
    if location == 'garden':
        garden(usrName, usrGendr, location)
    elif location == 'Home':
        home(usrName, usrGendr, location)
    elif location == 'North':
        north(usrName, usrGendr, location)
    elif location == 'North_West':
        north_west(usrName, usrGendr, location)
    elif location == 'West':
        west(usrName, usrGendr, location)
    elif location == 'South_West':
        south_west(usrName, usrGendr, location)
    elif location == 'South':
        south(usrName, usrGendr, location)
    elif location == 'South_East':
        south_east(usrName, usrGendr, location)
    elif location == 'East':
        east(usrName, usrGendr, location)
    elif location == 'DarkLands':
        darklands(usrName, usrGendr, location)
    elif location == 'Wildland':
        wildlands(usrName, usrGendr, location)
    elif location == 'Tower':
        tower(usrName, usrGendr, location)


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
    #     # so prorgram knows what to have and not?
