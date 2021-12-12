grid = []
with open("day11/input.txt") as f:
	for line in f:
		grid.append( list(map(int, [c for c in line.strip()])) )
print(grid)


# PART 1
flashes = 0
def check(grid):
	has_more_than_9 = False
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] > 9:
				has_more_than_9 = True
				break
	return has_more_than_9

# for t in range(100):
# 	# +1 to all energy
# 	for y in range(len(grid)):
# 		for x in range(len(grid[y])):
# 			grid[y][x] += 1
	
# 	# check for flashes, and affect surrounding
# 	flasheds = []
# 	while check(grid):
# 		for y in range(len(grid)):
# 			for x in range(len(grid[y])):
# 				if grid[y][x] > 9:
# 					if (y,x) not in flasheds:
# 						grid[y][x] = 0
# 						flashes += 1
# 						flasheds.append( (y,x) )
# 					if 0 <= y-1:
# 						if 0 <= x-1 and (y-1, x-1) not in flasheds: 
# 							grid[y-1][x-1] += 1
# 						if (y-1, x) not in flasheds: 
# 							grid[y-1][x] += 1
# 						if x+1 < len(grid[y-1]) and (y-1, x+1) not in flasheds:
# 							grid[y-1][x+1] += 1
					
# 					if 0 <= x-1 and (y, x-1) not in flasheds: 
# 						grid[y][x-1] += 1
# 					if x+1 < len(grid[y]) and (y, x+1) not in flasheds: 
# 						grid[y][x+1] += 1
					
# 					if y+1 < len(grid):
# 						if 0 <= x-1 and (y+1, x-1) not in flasheds:
# 							grid[y+1][x-1] += 1
# 						if (y+1, x) not in flasheds: 
# 							grid[y+1][x] += 1
# 						if x+1 < len(grid[y+1]) and (y+1, x+1) not in flasheds: 
# 							grid[y+1][x+1] += 1

# 	print("day", t+1)
# 	print(grid)
# print(flashes)


# PART 2
t = 0
found_day = False
while not found_day:
	# +1 to all energy
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			grid[y][x] += 1
	
	# check for flashes, and affect surrounding
	flasheds = []
	while check(grid):
		for y in range(len(grid)):
			for x in range(len(grid[y])):
				if grid[y][x] > 9:
					if (y,x) not in flasheds:
						grid[y][x] = 0
						flashes += 1
						flasheds.append( (y,x) )
					if 0 <= y-1:
						if 0 <= x-1 and (y-1, x-1) not in flasheds: 
							grid[y-1][x-1] += 1
						if (y-1, x) not in flasheds: 
							grid[y-1][x] += 1
						if x+1 < len(grid[y-1]) and (y-1, x+1) not in flasheds:
							grid[y-1][x+1] += 1
					
					if 0 <= x-1 and (y, x-1) not in flasheds: 
						grid[y][x-1] += 1
					if x+1 < len(grid[y]) and (y, x+1) not in flasheds: 
						grid[y][x+1] += 1
					
					if y+1 < len(grid):
						if 0 <= x-1 and (y+1, x-1) not in flasheds:
							grid[y+1][x-1] += 1
						if (y+1, x) not in flasheds: 
							grid[y+1][x] += 1
						if x+1 < len(grid[y+1]) and (y+1, x+1) not in flasheds: 
							grid[y+1][x+1] += 1

	temp_check = True
	for row in grid:
		for e in row:
			temp_check = temp_check and e == 0
			if temp_check == False:
				break
	if temp_check: found_day = True
	
	print("day", t+1)
	print(grid)

	t += 1

print(found_day)