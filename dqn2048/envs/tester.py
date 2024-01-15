"""def move_right(my_list):
    zero_count = my_list.count(0)
    non_zero_elements = [x for x in my_list if x != 0]
    return [0] * zero_count + non_zero_elements

my_list = [1, 2, 0, 4, 0, 6, 0]
result = move_right(my_list)
print(result)

def check_adjacent_tiles(row):
    adjacent_tiles = []
    
    # Iterate through the row from right to left
    for i in range(len(row) - 1, 0, -1):
        current_tile = row[i]
        
        # Check the tile to the left
        left_tile = row[i - 1] if i - 1 >= 0 else None
        
        # Append the current and left tiles to the adjacent_tiles list
        adjacent_tiles.append((current_tile, left_tile))
    
    return adjacent_tiles

# Example usage with a row
row = [1, 2, 0, 4, 0, 6, 0]
result = check_adjacent_tiles(row)
print(result)
print()"""

mergetest = [[2,0,0,2], [2,16,16,16], [4,4,4,4], [2,0,0,0]]

def applymerge(grid):
    #makes a move to the right, following 2048 rules (I think)
    def move_right(my_list):
      zero_count = my_list.count(0)
      non_zero_elements = [x for x in my_list if x != 0]
      return [0] * zero_count + non_zero_elements
    def merge(row):
      thisrow = row[::-1]
      for i in range(len(thisrow) - 1):
        if thisrow[i] != 0 and thisrow[i] == thisrow[i+1]:
           thisrow[i] = thisrow[i]*2
           thisrow[i+1] = 0
      row = thisrow[::-1]
      return row
    
    oldgrid = grid #for later comparison
    newgrid = []
    # Move all the way to the right every time
    reward = 0
    for row in grid:
      #if empty, pass
      if (sum(row) == 0):
        continue
      #move all tiles all the way to the right
      row = move_right(row)
      row = merge(row)    
      row = move_right(row)
      newgrid.append(row)
    
    if oldgrid != newgrid:
      pass#self.new_tile(1)

    print(reward)
    print(newgrid)
    return grid, reward

applymerge(mergetest)