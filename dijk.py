# Dijkstra's algorithm implementation
# M Danlowski (github.com/mdanlowski)
'''
		  _6_(A)_1__
	     /	  | 	\
(START)-<     3      >-(FINISH)
		 \_2__|__5__/
		 	 (B)				note: b>a but not a>b
'''

graph = {
	"start" : { "a" : 6 , "b" : 2 },
	"a"		: { "finish" : 1 },
	"b"		: { "a" : 3, "finish" : 5 } 
}
costs = {
	"a" : 6,
	"b" : 2
}
parents = {
	"a" : "start",
	"b" : "start"
}

# print(graph)
rootkeys = graph.keys()
# print(len(rootkeys))

for key in rootkeys:
	print(key, graph[key])
	for k in graph[key].keys():
		print(k, graph[key][k])

