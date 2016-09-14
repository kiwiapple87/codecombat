# You need to find and kill 3 skeletons.
# Skeletons and useful items can be summoned in the points of Power.
# You should move to the point and say the spell "VENI".
# To find the required points use the map from the wizard.
# 0 is a wrong point. Positive numbers are skeletons or useful items.

spell = "VENI"
# The map of points is represented as 2d array of numbers.
wizard = hero.findNearest(hero.findFriends())
powerMap = wizard.powerMap

# This function convert grid coordinates to x-y coordinates.
def convert(row, col):
    return {'x': 16 + col * 12, 'y': 16 + row * 12}

# You need loop through powerMap and find all positive numbers.
# First, loop through indexes of rows.
for i in range(len(powerMap)):
    # Each row is an array. Iterate through it.
    for j in range(len(powerMap[i])):
# Get the value of the i-th row and j-th column.
        pointValue = powerMap[i][j]
        hero.say(pointValue)
        hero.say("next")
        # If it's a positive number:
        if pointValue > 0:
        # Use the 'convert' function to get coordinates.
            pos = convert(i,j)
            # Move there, say "VENI", fight or pick up an item.
            hero.moveXY(pos.x, pos.y)
            hero.say("VENI")
            item = hero.findNearest(hero.findItems())
            enemy = hero.findNearest(hero.findEnemies())
            if enemy:
                hero.attack(enemy)
            else:
                hero.moveXY(item.pos.x, item.pos.y)
