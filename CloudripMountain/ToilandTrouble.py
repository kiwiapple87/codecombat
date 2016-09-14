# Ogre Witches have some unpleasant surprises ready for you.

# Define a chooseTarget function which takes a friend argument
# Returns the a target to attack, depending on the type of friend.
# Soldiers should attack the witches, archers should attack nearest enemy.

def chooseTarget(friend):
  witch = friend.findNearest(hero.findByType("witch"))
  nearest = friend.findNearest(hero.findEnemies())
  if friend.type == "soldier" and witch:
    return witch
  else:
    return nearest
  if friend.type == "archer":
    return nearest

while True:
    friends = hero.findFriends()
    for friend in friends:
        # Use your chooseTarget function to decide what to attack.
        target = chooseTarget(friend)
        hero.command(friend, "attack", target)
        pass
