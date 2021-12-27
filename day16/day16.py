hx = ""
with open("day16/input.txt") as f:
	hx = f.readline().strip()

binary = lambda x: "".join(reversed( [i+j for i,j in zip( *[ ["{0:04b}".format(int(c,16)) for c in reversed("0"+x)][n::2] for n in [1,0] ] ) ] ))

bn = binary(hx)

print(bn[0:3])
print(int(bn[:3], 2))
print(bn)

vsum = 0
parsables = 99999

# given up: this bs cant pass the 2nd and 3rd test cases

def parse(s):
	global vsum, parsables
	version = int(s[0:3], 2)

	vsum += version
	if parsables == 0: 
		parsables = 99999
		return
	parsables -= 1

	tid = int(s[3:6], 2)
	if tid == 4:
		# parse as literal
		# split into chunks of 5
		chunks = [ s[i:i+5] for i in range(6, len(s), 5) ]
		print("chonks", chunks)
		final = ""
		for i in range(len(chunks)):
			chunk = chunks[i]
			if len(chunk) == 5: final += chunk[1:]
			if chunk[0] == "0":
				others = "".join(chunks[i+1:])
				if len(others) != 0: parse(others)
				break  
		# final = "".join([ c[1:] for c in chunks if len(c) == 5 ])
		final = int(final, 2)
		print(final)
	else:
		# parse as operator
		length_id = s[6]
		if length_id == "0":
			# read next 15 bits
			total_length = int(s[7:22], 2)
			print("totallength", total_length)
			# break into mini chunks
			sub_packets = s[22:22+total_length]
			print("subpackets", sub_packets)
			parse(sub_packets)
		else:
			# read next 11 bits
			n_packets = int(s[7:18], 2)
			print("packets", n_packets)
			parsables = n_packets
			# break into mini chunks and parse
			sub_packets = s[18:]
			print('others', sub_packets)
			parse(sub_packets)
			

parse(bn)

print(vsum)