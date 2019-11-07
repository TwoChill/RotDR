import base


# usrName = ''
# mentorName = ''
# usrGendr = ''
# usrGendr_boy = ("he", "his", "him", "his",
#                 "He", "His", "Him", "His")
# usrGendr_girl = ("she", "hers", "her", "her",
#                  "She", "Hers", "Her", "Her")


class Game_Text(base.Hero):

    def __init__(self, usrName, usrGendr, mentorName, location):
        super().__init__(usrName, usrGendr)


def game_text(usrName, usrGendr, mentorName, location):
    ''' Returns text to @@@ '''

    tutorial_text_1 = f''' ALLA
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
    return tutorial_text_1

    tutorial_text_2 = f'''
  {usrName} looks around at the {location}
  and sees a big tree inside a grass field
  surrounded by a man-made wooden fence.

  There's a wooden chop-block at the end of the grassfield
  next to a stands sturdy man-made wooden log.

  A feeling of familiarity came over {usrName} as {usrGendr[0]} sees
  {usrGendr[3]} mentor standing in the doorway of the log.
  '''
    return tutorial_text_2

    tutorial_text_3 = f'''
  With a confused face, {mentorName} walks up to {usrName}
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
    return tutorial_text_3

    tutorial_text_4 = f'''
  {mentorName} pukes from excaustion!
  But he looks happy...
  Probably beacuse you can help find his map now.\n
  '''
    return tutorial_text_4
