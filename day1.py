# https://adventofcode.com/2021/day/1/input
# print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
data = []
while True:
	try:
		line = int(input())
	except EOFError:
		break
	data.append(line)
print(data)


### PART 1
inc = 0
for i in range(len(data)-1):
	if (data[i] < data[i+1]): inc += 1
print(inc)


### PART 2
inc = 0
for i in range(len(data)-3):
	window1 = data[i] + data[i+1] + data[i+2]
	window2 = data[i+1] + data[i+2] + data[i+3]

	if (window1 < window2): inc += 1
print(inc)