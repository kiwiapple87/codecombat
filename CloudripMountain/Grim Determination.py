# Your goal is to protect Reynaldo

# Find the paladin with the lowest health.
def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.type != "paladin":
            continue
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend

def commandPaladin(paladin):
    # Heal the paladin with the lowest health using lowestHealthPaladin()
    # You can use paladin.canCast("heal") and command(paladin, "cast", "heal", target)
    # Paladins can also shield: command(paladin, "shield")
    # And don't forget, they can attack, too!
    halfHealth = paladin.maxHealth / 2
    friend = lowestHealthPaladin()
    enemy = paladin.findNearest(hero.findEnemies())
    if paladin.canCast("heal"):
        hero.command(paladin, "cast", "heal", friend)
    elif paladin.health < halfHealth:
        hero.command(paladin, "shield")
    elif enemy:
        hero.command(paladin, "attack", enemy)
    pass

def commandFriends():
    # Command your friends.
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "peasant":
            #commandPeasant(friend)
            pass
        elif friend.type == "griffin-rider":
            #commandGriffin(friend)
            pass
        elif friend.type == "paladin":
            commandPaladin(friend)

while True:
    commandFriends()
    # Summon griffin riders!
