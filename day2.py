# https://adventofcode.com/2021/day/2/input
# print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
instructions = []
while True:
	try:
		line = input()
	except EOFError:
		break
	instructions.append(line)
print(instructions)


### PART 1
hor, dep = 0, 0
for i in instructions:
	value = int(i.split(" ")[-1])
	if ("forward" in i): hor += value
	elif ("down" in i): dep += value
	elif ("up" in i): dep -= value
print(hor*dep)


### PART 2
hor, dep, aim = 0, 0, 0
for i in instructions:
	value = int(i.split(" ")[-1])
	if ("forward" in i): 
		hor += value
		dep += aim*value
	elif ("down" in i):
		aim += value
	elif ("up" in i):
		aim -= value
print(hor*dep)



