# https://adventofcode.com/2021/day/8
signals = []
outputs = []
with open("day8/input.txt") as f:
	for line in f:
		_line = line.split(" | ")
		signals.append(_line[0])
		outputs.append(_line[1].replace("\n", ""))


### PART 1
# total = 0
# for output in outputs:
# 	print(output.split(" "))
# 	for token in output.split(" "):
# 		if (len(token) in [2, 4, 3, 7]):
# 			total += 1
# print(total)


### PART 2
def find_of_length(arr, length):
	return [x for x in arr if len(x) == length]

def find_fully_contains(arr, want):
	# find ans which fully contains "want"
	ans = ""
	for token in arr:
		check = True
		for segment in want:
			check = check and segment in token
		if check: ans = token
	return ans

total_sum = 0
for idx, signal in enumerate(signals):
	tokens = signal.split(" ")
	mappings = {i : -1 for i in tokens}

	# method: find 7 first
	# then find 3 (is contained)
	# then use 3 to find 2; will leave 5 behind w/ no confusion
	# again, use 3 to find 9 (is contained)

	[one] = find_of_length(tokens, 2)
	[four] = find_of_length(tokens, 4)
	[seven] = find_of_length(tokens, 3)
	[eight] = find_of_length(tokens, 7)
	mappings[one] = 1
	mappings[four] = 4
	mappings[seven] = 7
	mappings[eight] = 8

	five_segments = find_of_length(tokens, 5) # could be 2, 3, 5
	six_segments = find_of_length(tokens, 6) # could be 0, 6, 9

	# find 3
	three = find_fully_contains(five_segments, seven)
	five_segments.remove(three)

	# find 5 by comparing with four
	five = ""
	for token in five_segments:
		same_segments = 0
		for segment in four:
			if segment in token: same_segments += 1
		if same_segments == 3:
			five = token
	five_segments.remove(five)

	# 2 is the only one left
	[two] = five_segments

	# find 9
	nine = find_fully_contains(six_segments, three)
	six_segments.remove(nine)

	# find 6
	six = find_fully_contains(six_segments, five)
	six_segments.remove(six)

	# 0 is the only one left
	[zero] = six_segments
	
	mappings[zero] = 0
	mappings[two] = 2
	mappings[three] = 3
	mappings[five] = 5
	mappings[six] = 6
	mappings[nine] = 9

	output = outputs[idx]
	
	num = []
	for token in output.split(" "):
		for key, value in mappings.items():
			if sorted(key) == sorted(token):
				num.append(value)

	length = len(num)
	for idx, digit in enumerate(num):
		total_sum += digit * (10**(length - 1 - idx))
	
print(total_sum)