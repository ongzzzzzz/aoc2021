graph = {}
with open("day12/input.txt") as f:
	for line in f:
		l = line.strip().split('-')
		try:
			graph[l[0]].append(l[1])
		except KeyError:
			graph[l[0]] = [l[1]]

		try:
			graph[l[1]].append(l[0])
		except KeyError:
			graph[l[1]] = [l[0]]
		
print(graph)


# PART 1
# visiteds = {i:0 for i in graph.keys()}
# paths = set()
# curr_path = []

# def find_end(curr_node):
# 	global visiteds, paths, curr_path

# 	if curr_node == "end":
# 		paths.add(",".join(curr_path))
# 		return
	
# 	if curr_node == curr_node.lower():
# 		if visiteds[curr_node] >= 1:
# 			return
	
# 	visiteds[curr_node] += 1
	
# 	curr_path.append(curr_node)
# 	for node in graph[curr_node]:
# 		find_end(node)
# 	curr_path.pop()

# 	visiteds[curr_node] -= 1


# find_end("start")
# print(visiteds)
# for path in paths:
# 	print(path)
# print(len(paths))


# PART 2
visiteds = {i:0 for i in graph.keys()}
paths = set()
curr_path = []
def find_end(curr_node):
	global visiteds, paths, curr_path

	if curr_node == "end":
		paths.add(",".join(curr_path))
		return
	
	if curr_node == curr_node.lower():
		
		# if visited once, check if other got visit twice?
		if visiteds[curr_node] == 1:
			for key, value in visiteds.items():
				if key == key.lower() and value == 2 and key != curr_node:
					return
		# already max, cant visit again
		if visiteds[curr_node] == 2:
			return
	
	visiteds[curr_node] += 1
	
	curr_path.append(curr_node)
	for node in graph[curr_node]:
		find_end(node)
	curr_path.pop()

	visiteds[curr_node] -= 1


find_end("start")
# print(visiteds)
final_paths = []
# remove paths with double "start"
for path in paths:
	if path.split(",").count("start") == 1:
		final_paths.append(path)
# for path in final_paths:
# 	print(path)
print(len(final_paths))