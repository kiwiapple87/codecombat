def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)

# remove fast
def moveTo(position):
    if (self.isReady("jump") and self.distanceTo > 10):
        self.jumpTo(position)
    else:
        self.move(position)

# remove bash and power up 
def attack(target):
    if target:
        if (self.distanceTo(target) > 10):
            moveTo(enemy.pos)
        else:
            self.attack(enemy)


summonTypes = ['soldier', 'soldier', 'griffin-rider', 'soldier', 'archer']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


# commands attack - may have to focus on enemy types
def commandSoldiers():
    for soldier in self.findFriends():
        enemy = soldier.findNearest(hero.findEnemies())
        if enemy:
            self.command(soldier, "attack", enemy)


while True:
    summonTroops()
    commandSoldiers()
    items = self.findItems()
    if (len(items) > 0 or (enemy and hero.distanceTo(enemy) > 10)):
        pickUpNearestItem(items)
    else:
        attack(enemy)
