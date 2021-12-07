# https://adventofcode.com/2021/day/6/input
fishes = list(map(int, open("day6/input.txt").read().split(",")))


### PART 1
# T = 80 # run for 80 days
# for t in range(T):
# 	next_gen_of_fishes = []
# 	for f in fishes:
# 		if f > 0:
# 			# not yet going to breed, decrement fish timer by 1 
# 			next_gen_of_fishes.append(f - 1)
# 		else:
# 			# breeded, reset to 6 and add new fish
# 			next_gen_of_fishes.append(6)
# 			next_gen_of_fishes.append(8)
# 	fishes = next_gen_of_fishes
# print(len(fishes))


### PART 2
T = 256
# keep track of count of fishes with diff timers
fishes_dict = {}
for f in fishes:
	if f in fishes_dict.keys(): fishes_dict[f] += 1
	else: fishes_dict[f] = 1
print(fishes_dict)

for t in range(T):
	new_fishes = {i : 0 for i in range(9)}

	for timer, count in fishes_dict.items():
		if timer > 0:
			new_fishes[timer - 1] += count
		else:
			new_fishes[6] += count
			new_fishes[8] += count
	fishes_dict = new_fishes
print(sum(fishes_dict.values()))