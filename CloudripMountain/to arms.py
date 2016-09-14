# Ogres are going to attack soon.
# Move near each of tents (to the X marks)
# say() something at each X to wake your soldiers.
# Beware: leave the camp when the battle begins!
# Ogres will send reinforcements if they see the hero.

# The sergeant knows the distance between tents.
sergeant =  hero.findNearest(hero.findFriends())

# The distances between the X marks.
stepX = sergeant.tentDistanceX
stepY = sergeant.tentDistanceY
# The number of tents.
tentsInRow = 5
tentsInColumn = 4

# The first tent mark has constant coordinates.
firstX = 10
firstY = 14

# Use nested loops and visit all 20 tents.
# IMPORTANT: move row by row - it's faster.
for i in tentsInRow:
    for j in tentsInColumn:
        # Move at the marks near tents and say anything.
        hero.moveXY(firstX + (j*21), firstY + (i*12))

# Now watch the battle.
hero.moveXY(21,6)
