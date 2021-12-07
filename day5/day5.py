# https://adventofcode.com/2021/day/5
import numpy as np

floor = []
mappings = []
max_x = 0
max_y = 0
with open("day5/input.txt") as f:
	for line in f:
		line = line.split(" -> ")
		line = [x.split(",") for x in line]
		line = [ list(map(int, line[0])), list(map(int, line[1])) ]
		max_x = max( max_x, line[0][0], line[1][0] )
		max_y = max( max_y, line[0][1], line[1][1] )
		
		mappings.append(line)


### PART 1
# floor = list(map(list, list(np.zeros([max_x+1, max_y+1], dtype=int))))
# print("grid size:", max_x+1, max_y+1)

# for mapping in mappings:
# 	c_from = mapping[0]
# 	c_to = mapping[1]
	
# 	if (c_from[0] == c_to[0]):
# 		# if x coord same (vertical line)
# 		for y in range(min(c_from[1], c_to[1]), max(c_from[1], c_to[1])+1):
# 			floor[y][c_from[0]] += 1
# 	elif (c_from[1] == c_to[1]):
# 		# if y coord same (horizontal line)
# 		for x in range(min(c_from[0], c_to[0]), max(c_from[0], c_to[0])+1):
# 			floor[c_from[1]][x] += 1

# count = 0
# for c in floor:
# 	for r in c:
# 		if r >= 2:
# 			count += 1
# print(count)
	

### PART 2
floor = list(map(list, list(np.zeros([max_x+1, max_y+1], dtype=int))))
print("grid size:", max_x+1, max_y+1)

for mapping in mappings:
	c_from = mapping[0]
	c_to = mapping[1]

	_min_x = min(c_from[0], c_to[0])
	_min_y = min(c_from[1], c_to[1])

	_max_x = max(c_from[0], c_to[0])
	_max_y = max(c_from[1], c_to[1])
	
	if (c_from[0] == c_to[0]):
		# if x coord same (vertical line)
		for y in range(_min_y, _max_y + 1):
			floor[y][c_from[0]] += 1
	elif (c_from[1] == c_to[1]):
		# if y coord same (horizontal line)
		for x in range(_min_x, _max_x+1):
			floor[c_from[1]][x] += 1
	else:
		# both coord different, diagonal line
		# start with the one with min x value
		if (c_from[0] > c_to[0]):
			temp = c_from
			c_from = c_to
			c_to = temp
		start = c_from
		# then diag-down or diag-up depending on y value of other point
		floor[c_from[1]][c_from[0]] += 1
		while (c_from != c_to):
			c_from[0] += 1
			c_from[1] += (1 if c_from[1] < c_to[1] else -1)
			floor[c_from[1]][c_from[0]] += 1
# print(floor)
count = 0
for c in floor:
	for r in c:
		if r >= 2:
			count += 1
print(count)