start = ""
pairs = {}
with open("day14/input.txt") as f:
	start = f.readline().strip()
	f.readline()
	for line in f:
		l = line.strip().split(" -> ")
		pairs[l[0]] = l[1]

print(start)


# PART 1
# for t in range(10):
# 	final = ""
# 	final += start[0]
# 	for i in range(len(start)-1):
# 		a, b = start[i], start[i+1]
# 		final += pairs[a+b]
# 		final += b
# 	start = final

# elements = {}
# for c in final:
# 	try:
# 		elements[c] += 1
# 	except KeyError:
# 		elements[c] = 1

# counts = elements.values()
# print(max(counts) - min(counts))


# PART 2
print(start)
print(pairs)
counts = {}

for i in range(len(start)-1):
	pair = start[i] + start[i+1]
	try: 
		counts[pair] += 1
	except KeyError:
		counts[pair] = 1


for t in range(40):
	temp = {}
	for pair in counts.keys():
		new = pairs[pair]
		new_pair_1 = pair[0] + new
		new_pair_2 = new + pair[1]

		try: temp[new_pair_1] += counts[pair]
		except KeyError: temp[new_pair_1] = counts[pair]
		
		try: temp[new_pair_2] += counts[pair]
		except KeyError: temp[new_pair_2] = counts[pair]
	counts = temp
# print(counts)

# convert pairs to letters
letters = {}

first = list(counts.keys())[0]
letters[first[0]] = counts[first] # just the first letter of first pair

for pair, count in counts.items():
	letter = pair[1]
	try: 
		letters[letter] += count
	except KeyError:
		letters[letter] = count
	
letter_counts = list(letters.values())
letter_counts.sort()
print(letter_counts[-1] - letter_counts[0])