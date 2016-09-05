# Robobombs explode when they die or touch an enemy.
# Split up your soldiers so that they don't all get exploded together.
pos = {"x": 8, "y": 15}
while True:
    enemies = hero.findEnemies()
    enemy = hero.findNearest(enemies)
    friends = hero.findFriends()
    # Send the first soldier of the friends array towards the enemy.
    hero.command(friends[0], "attack", enemy)
    # i in range(1, n) starts the index at the second element!
    for i in range(1, len(friends)):
        friend = friends[i];
        # Command the remaining soldiers to run away!
        hero.command(friend, "move", pos)
