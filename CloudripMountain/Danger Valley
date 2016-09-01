# Ogres have taken some peasants hostage!
# Your scouts have given you the intel required to lay an ambush.
# this.grid holds an array of arrays.
# Inside these sub-arrays, 0 is a peasant and 1 is an ogre!
# Use this information to setup fire-traps to defeat the convoy.

# First, remember the containing array is just an array!
# Iterate over all the elements of this array.
for i in range(len(hero.grid)):
    row = hero.grid[i]
    # Now, row is just another array!
    # Iterate over all the tiles in this array:
    for j in range(len(row)):
        # Do a check to see if the tile of row i at j is 1.
        tile = row[j]
        if tile == 1:    
            hero.buildXY("fire-trap", 36 + 6 * j, 20 + 6 * i)
        
            
# Finally, retreat back to cover.
hero.moveXY(29, 55)
