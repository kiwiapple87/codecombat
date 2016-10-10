# Fight your way into the Inner Sanctum of the ogre chieftain, and kill her.
# Breach the outer gate
# Breach the Inner gate
# Reach the Inner Sanctum
# Ogres must die (26/63)

def commandSoldiers(soldiers):
    for soldier in soldiers:
        nearest = soldier.findNearest(hero.findEnemies())
        if soldier.type == "paladin":
            if solder.isReady("heal"):
                friend = lowestHealth(soldiers) 
                hero.command(soldier, "heal", friend)
            else:
                hero.command(soldier, "attack", nearest)
        else:
            hero.command(soldier, "attack", nearest)
        
def lowestHealth(soldiers):
    lowHealth = 99999
    friend = None
    for soldier in soldiers:
        if soldier.health < lowHealth:
            friend = soldier
            lowHealth = soldier.health
    return friend
        

While True:
    friends = hero.findFriends()
    commandSoldiers(friends)
