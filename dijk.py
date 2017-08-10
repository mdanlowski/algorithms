processed = []

def next_lowest_cost_node( costs_table ):
    lowest_cost = float("inf")
    lowest_node = None
    for node in costs_table:
        current_cost = costs_table[node]
        if current_cost < lowest_cost and node not in processed:
            lowest_cost = current_cost
            lowest_node = node
    # print(lowest_node)
    return lowest_node
         

graph = {
	'start' : { 'a' : 6, 'b' : 2 },
	'a' : { 'finish' : 1 },
	'b' : { 'a' : 3, 'finish' : 5 },
	'finish' : {}
}
costs = {
	'a' : 6,
	'b' : 2,
	'finish' : float('inf')
}
parents = {
	'start' : None,
	'a' : 'start',
	'b' : 'start',
	'finish' : None
}

node = next_lowest_cost_node(costs)
while node is not None:
	cost = costs[node]
	nebrs = graph[node]
	for n in nebrs.keys():
	    new_cost = cost + nebrs[n]
	    if new_cost < costs[n]:
	        costs[n] = new_cost
	        parents[n] = node
	processed.append(node)
	node = next_lowest_cost_node(costs)   

path = ''
elem = 'finish'
while elem != None:
	if elem == 'start': path += elem
	else: path += (elem + " <-- ")
	elem = parents[elem]
 
print("Path:  " + path)
print("Cost: ", costs['finish'])

# print(costs)

