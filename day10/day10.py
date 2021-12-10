lines = []
with open("day10/input.txt") as f:
	for line in f:
		l = line.strip()
		lines.append(l)

openings = "([{<"
closings = ")]}>"

incomplete_lines = lines.copy()

# PART 1
pts = 0
for line in lines:
	stack = []
	for c in line:
		if c in openings:
			stack.append(c)
		else:
			error = ""
			# char is closing; if illegal, error
			for i, closing in enumerate(closings):
				if c == closing:
					if stack[-1] == openings[i]: stack.pop()
					else: 
						error = c
						break
			if error != "":
				# print(error_char)
				# print(line)
				# print("error", stack, c)
				if error == ")": pts += 3
				if error == "]": pts += 57
				if error == "}": pts += 1197
				if error == ">": pts += 25137
				incomplete_lines.remove(line)
				break
print(pts)


# PART 2
scores = []
for line in incomplete_lines:
	stack = []
	for c in line:
		if c in openings:
			stack.append(c)
		else:
			# can safely do so since its not a corrupted line
			stack.pop()

	stack = list(reversed(stack))
	remaining = "".join([ closings[ openings.find(x) ] for x in stack ])
	# print(remaining)

	score = 0
	for c in remaining:
		score *= 5
		score += (closings.find(c)+1)
	scores.append(score)

scores.sort(reverse=True)
print(scores[len(scores)//2])