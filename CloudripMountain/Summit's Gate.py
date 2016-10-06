# Fight your way into the Inner Sanctum of the ogre chieftain, and kill her.
# Breach the outer gate
# Breach the Inner gate
# Reach the Inner Sanctum
# Ogres must die (26/63)

def commandSoldiers(soldier):
    if soldier.type == "paladin":
        #heal is ready cast heal on lowest health friend else attack
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
    nearest = hero.findNearest(hero.findEnemies())
    friends = hero.findFriends()
