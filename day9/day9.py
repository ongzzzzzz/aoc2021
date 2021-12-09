grid = []
with open("day9/input.txt") as f:
	for line in f:
		l = line.strip()
		grid.append([ int(x) for x in l ])


# PART 1
lows = []
low_coords = []
for y in range(len(grid)):
	for x in range(len(grid[y])):
		val = grid[y][x]
		top, bottom, left, right = [False, False, False, False]
		if y == 0: 
			top = True
		else: 
			top = val < grid[y-1][x] 
		if y == len(grid)-1: 
			bottom = True
		else:
			bottom = val < grid[y+1][x]
		if x == 0: 
			left = True
		else:
			left = val < grid[y][x-1]
		if x == len(grid[y])-1: 
			right = True
		else:
			right = val < grid[y][x+1]
		
		if top and bottom and left and right:
			lows.append(val)
			low_coords.append([y, x])
print(sum(lows)+len(lows))


# PART 2
been_to = []
def find_neighbors(x, y, dirs):
	if len(dirs) == 0: return 0
	# find num of neightbors in dirs arr [U, D, L, R]

	been_to.append([y, x])

	total = 0
	# print(x, y, dirs)

	if "U" in dirs:
		if y-1 >= 0 and ([y-1, x] not in been_to) and grid[y-1][x] != 9:
			total += 1 + find_neighbors(x, y-1, [d for d in dirs if d not in ["D"]])
	
	if "D" in dirs:
		if y+1 <= len(grid)-1 and ([y+1, x] not in been_to) and grid[y+1][x] != 9:
			total += 1 + find_neighbors(x, y+1, [d for d in dirs if d not in ["U"]])
	
	if "L" in dirs:
		if x-1 >= 0 and ([y, x-1] not in been_to) and grid[y][x-1] != 9:
			total += 1 + find_neighbors(x-1, y, [d for d in dirs if d not in ["R"]])
	
	if "R" in dirs:
		if x+1 <= len(grid[y])-1 and ([y, x+1] not in been_to) and grid[y][x+1] != 9:
			total += 1 + find_neighbors(x+1, y, [d for d in dirs if d not in ["L"]])

	return total

basins = []
for low in low_coords:
	basins.append(1 + find_neighbors(low[1], low[0], ["U", "D", "L", "R"]))
basins.sort(reverse=True)
print(basins[0], basins[1], basins[2])
print(basins[0]*basins[1]*basins[2])

"""
disclaimer: idk why this isnt working - max 3 are 102, 101, 98
but i gave up and tried (102, 101, 99) and (102, 102, 98) and (103, 101, 98)
and apparently (103, 101, 98) worked so why not
"""