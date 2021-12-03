# https://adventofcode.com/2021/day/3/input
# print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
binaries = []
while True:
	try:
		line = input()
	except EOFError:
		break
	binaries.append(line)
print(binaries)


### PART 1
bin_len = len(binaries[0])
num_of_1s_in_bit = [0]*bin_len

for b in binaries:
	for i in range(bin_len):
		if (b[i] == '1'):
			num_of_1s_in_bit[i] += 1
print(num_of_1s_in_bit)
print(len(binaries))

gam, eps = "", ""
for n1 in num_of_1s_in_bit:
	if (n1 < 0.5*len(binaries)):
		# least common bit = 1
		gam += "0"
		eps += "1"
	else:
		# least common bit = 0
		gam += "1"
		eps += "0"
# # print(gam, eps)
gam, eps = int(gam, 2), int(eps, 2)
print(gam * eps)


### PART 2
# o2 generator rating
filtered_bins = binaries
for i in range(bin_len):
	if len(filtered_bins) > 1:
		num_1s_in_pos = sum([1 for b in filtered_bins if b[i]=='1'])
		desired_bit = '0' if num_1s_in_pos < 0.5*len(filtered_bins) else '1'
		filtered_bins = [b for b in filtered_bins if b[i] == desired_bit]
o2 = filtered_bins[0]

# co2 scrubber rating
filtered_bins = binaries
for i in range(bin_len):
	if len(filtered_bins) > 1:
		num_1s_in_pos = sum([1 for b in filtered_bins if b[i]=='1'])
		desired_bit = '1' if num_1s_in_pos < 0.5*len(filtered_bins) else '0'
		filtered_bins = [b for b in filtered_bins if b[i] == desired_bit]
co2 = filtered_bins[0]

o2, co2 = int(o2, 2), int(co2, 2)
print(o2 * co2)