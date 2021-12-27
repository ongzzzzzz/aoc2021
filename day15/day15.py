import numpy as np
grid = []
with open("day15/input.txt") as f:
	for line in f:
		grid.append([int(x) for x in line.strip()])

print(grid)


# PART 1
# create cost grid of same dimension
risks = list(map(list, list(np.zeros([len(grid), len(grid[0])], dtype=int))))
risks[0][0] = grid[0][0]

# fill in top row
for x in range(1, len(grid[0])):
	risks[0][x] = risks[0][x-1] + grid[0][x]

# fill in left col
for y in range(1, len(grid)):
	risks[y][0] = risks[y-1][0] + grid[y][0]

# fill in everything else
for y in range(1, len(grid)):
	for x in range(1, len(grid[0])):
		risks[y][x] = grid[y][x] + min(risks[y-1][x], risks[y][x-1])

print(risks[-1][-1] - risks[0][0])
