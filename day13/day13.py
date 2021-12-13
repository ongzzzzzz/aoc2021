import numpy as np

coords = []
instructions = []
max_x, max_y = 0, 0
with open("day13/input.txt") as f:
	for line in f:
		if len(line.strip().split(",")) == 2:
			l = [int(x) for x in line.strip().split(",")]
			max_x = max(max_x, l[0])
			max_y = max(max_y, l[1])
			coords.append(l)
		else:
			l = line.strip().replace("fold along ", "").split("=")
			if len(l) > 1:
				instructions.append( [l[0], int(l[1])] )

paper = list(map(list, list(np.zeros([max_y+1, max_x+1], dtype=int))))
for coord in coords:
	paper[coord[1]][coord[0]] = 1
# print(max_x, max_y)


# PART 1
# 1st instruction is x=655
# i = instructions[0][1]
# for y in range(len(paper)):
# 	for x in range(i+1, max_x+1):
# 		paper[y][ i - (x-i) ] += paper[y][x]
# 		# print(y, i-(x-i))
# 	paper[y] = paper[y][:i]

# count = 0
# for row in paper:
# 	for e in row:
# 		if e > 0: count += 1
# print(count)


# PART 2
for instruction in instructions:
	i = instruction[1]
	if instruction[0] == "x":
		x_max = len(paper[0])
		for y in range(len(paper)):
			for x in range(i+1, x_max):
				paper[y][ i - (x-i) ] += paper[y][x]
				# print(y, i-(x-i))
			paper[y] = paper[y][:i]

	if instruction[0] == "y":
		for x in range(len(paper[0])):
			for y in range(i+1, len(paper)):
				# print(i-(y-i), x)
				# print(" ", y, x)
				paper[i-(y-i)][x]
				paper[y][x]
				paper[ i - (y-i) ][x] += paper[y][x]
				# print(y, i-(x-i))
		paper = paper[:i]

# print(paper)
for y in range(len(paper)):
	for x in range(len(paper[y])):
		if paper[y][x] != 0:
			paper[y][x] = "#"
		else:
			paper[y][x] = " "

for row in paper:
	print("".join(row))