from collections import deque  # double-ended queue

def bfsearch( graph, lookingfor ):
	src = deque()
	seen = []
	src += graph['you']
	qlen = 1  # 0 - self
	while src:
		curr = src.popleft()
		if not curr in seen:
			if evaluate( curr, lookingfor ):
				print("found! edges crossed: ", qlen)
				return True 
			else:
				seen.append(curr)
				src += graph[curr]
				qlen += 1
				print(seen)
				print(src)
	print("connection not found, edges crossed: ", qlen)
	return False
			

def evaluate( provided, lookingfor ):  # if True, graph search successful
	return provided == lookingfor


graph = {}	# using a dictionary to model connections 
			# in a directed graph
'''
		________you_______
	   /         |        \
	jon        marry       tim
  /    |      /    \         \
janet cary   ron carol      elon
			  |
			 ali
'''
graph['you'] = ['jon', 'marry', 'tim']
graph['jon'] = ['janet', 'cary']
graph['marry'] = ['ron', 'carol']
graph['tim'] = ['elon']
graph['janet'] = []
graph['cary'] = []
graph['ron'] = ['ali']
graph['carol'] = []
graph['elon'] = []
graph['ali'] = []

print(graph, '\n')

print(bfsearch(graph, 'ali'))