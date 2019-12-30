#######################################################################

iNput = ':> '
newLineInput = '\n:> '
tabInput = '\t:> '
dTabInput = '\t\t:> '
askGendr = "\n\t\tAre you a Boy or a Girl?"
chooseCharName = "\n\t\tChoose your characters Name:"
createBoy = '\n\n\t\tA Boy has been created!\n\n'
createGirl = '\n\n\t\tA Girl has been created!\n\n'
dubbleChkName = '\n\t\tIs "{}" correct? (Y/N):'
initChar = '\n\n\t\t{} has been created!\n\n\tInitialization: Started\n\nInitialize in:\n3 ...\n2 .. \n1 . \n'

#######################################################################

mentorName = "\n\n\t{} just woke up and rememberd {} mentor's name.."
noMentorName = "\nIt's been a rough nap... what was {} mentor's name?'\n"

Welcome_Menu = '''
                                                ############################
                                                #          {}         #
                                                ############################

                                                          - {} -
                                                          - {} -
                                                          - {} -

                                                          - {} -

                                                          Made by:
                                                      {}
                                                ############################
'''

Help_Menu = '''
                                                ############################
                                                #         - Help -         #
                                                ############################
                                                - Type commands to do them -

                                                          - {} -
                                                - "play" to start the game -

                                                          - {} -
                                                - "load" to load your game -

                                                          - {} -
                                                - "quit" to exit  the game -

                                                        - "{}" -

                                              - Press "CTRL" to speed up txt -
                                                - Good luck and have fun!! -
                                                ############################
'''
#######################################################################

obtain_text = "\n\t{}{}{} Obtains {}!{}"

#######################################################################

cmd_tutorial_txt = "\n\n# Tutorial: Use command {} #\n"
cmd_tutorial_look = "Type {} to look around your surroundings."
cmd_tutorial_dig = " Type {} to open a small black portal."
cmd_tutorial_map = "Type {} to see were you are."

#######################################################################

openigTxt = '''
            You are about to embark on a journey of the imagination.
                Full of everything your imagination can fill

                    .. With a helping  hand offcourse ..

                   .... So let's create a character! ....'''
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################

tutorial_text_1 = '''
{} slowly opens {} eyes from {} hammock.

The first thing {} notice
is the warm sun on {} face,
birds chirping faintly in the background,
and a lukewarm breeze,
that carries a sweet scent of primrose roses.

Peaceful..


After a few moments,
{} hears the sound of a door opening.
{} looks up and sees {} mentor standing in a doorway.
'''

#######################################################################

tutorial_text_2 = '''
{} looks around at the {}
and sees a big tree inside a grass field
surrounded by a man-made wooden fence.

There's a wooden chop-block at the end of the grass field
next to a stands sturdy man-made wooden log.

A feeling of familiarity came over {} as {} sees
{} mentor standing in the doorway of the log.
'''

#######################################################################

tutorial_text_3 = '''
With a confused face, {} walks up to {}
and he asks to help him find a map that he buried
somewhere around this {}.

You decide to help {}.
He places his hand on {} forehead,
while mumbling some kind of strange mantra.

While listening to the mantra, {} can't help but notice,
a strang thermic force coming of {} body.

Suddenly {} hand glows
and a rainbow-colored thermic force shoots out of his hand ...


A warm feeling came over {}.
'''

#######################################################################

tutorial_text_4 = '''
{} pukes from excaustion!
But he looks happy...

(Probably because you can help find his map now!)

{} puts {} hand on the ground..
The same rainbow-colored thermic force
shoots from {} arm through and out of his hand!

{} somehow opens a small black portal
with evaporating 1's and 0's around the edges.

{} hand went through the ground's dimension and {} felt something...
'''

#######################################################################

tutorial_text_5 = '\nIt was the map {} {}{}was looking for!{}'

#######################################################################

tutorial_text_6 = '''
{} turns around and gives the map to {} mentor.

With relieve {} looks at the map
and with a snap of his fingers, the map vanishes .. !?!

{} looks at {} and asks {} to use the map ..
'''
#######################################################################

# fake AI for Character Creation. !!DO NOT CHANGE THE LAST ITEM!!
fAI_CC = ['Just think of one strong name...',
          "It's just a cleaver combination of A's -> Z's ..",
          "'Zolar'?, 'Matt'?, I'm just trying to help ... ",
          "There must be something you can think of..",
          "Yes .. It's hard.. and forever. Sooo, take your time..",
          "..... -_-",
          "I have faith you'll succeed on your next try.. ",
          # "It's a thing now-a-day's.. I'll randomly pick a gender for you! ;)",
          "Look.. If it's a gender-neutral thing.. I mean..."]

#######################################################################
#
fAI = ['\t\t\tUhmm.. I think you misspelled..',
       "\t\t\t'{}', is kinda.. forein to me.",
       "\t\t\tNope, I didn't get that!",
       '\t\t\t.......... -_-',
       '\t\t\tWe all have brainfarts sometimes ....',
       "\t\t\tI don't think '{}' is the answer..",
       '\t\t\tOeps, brainfart! Again please!',
       "\t\t\tThat's just not correct.",
       "\t\t\tI'm sorry, but I don't know what '{}' means.",
       "\t\t\tThat's what she! said.",
       "\t\t\t.. 'help' could be usefull .."]

#######################################################################

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
#######################################################################
logo = '''
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

#######################################################################


#######################################################################


#######################################################################


#######################################################################


#######################################################################


#######################################################################
