# https://adventofcode.com/2021/day/7
crabs = [int(x) for x in open("day7/input.txt").read().split(",")]
crabs.sort()


### PART 1
positions = {}
for pos in range(min(crabs), max(crabs)+1):
	cost = 0
	# calculate fuel cost and store in positions
	for c in crabs:
		cost += abs(c - pos)
	positions[pos] = cost

min_pos = max(crabs) + 1
min_cost = max(positions.values())
for key, value in positions.items():
	if value < min_cost:
		min_cost = value
		min_pos = key
print(min_cost, "fuel needed to align to", min_pos)


### PART 2
positions = {}
for pos in range(min(crabs), max(crabs) + 1):
    cost = 0
    # calculate fuel cost and store in positions
    for c in crabs:
        dist_to_pos = abs(c - pos)
        # sum from 1 to dist_to_pos
        cost += (dist_to_pos) * (dist_to_pos + 1) / 2
    positions[pos] = cost

min_pos = max(crabs) + 1
min_cost = max(positions.values())
for key, value in positions.items():
    if value < min_cost:
        min_cost = value
        min_pos = key
print(min_cost, "fuel needed to align to", min_pos)
