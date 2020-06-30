import sys,heapq
class Vertex:
	def __init__(self,n):
		#Each vertex will have a few characteristics
		self.name = n 
		self.color = 'Black'
		self.previous = None #Set previous vertex to be none for now
		self.neighbours = {}
		self.distance = sys.maxsize

	def addNeighbour(self,v,weight):
		#Use this to add an edge to the graph 
		if v not in self.neighbours:
			self.neighbours[v] = weight #Distance between two nodes
			return True 

class Graph:
	#A class to implement the graph 
	vertices = {}

	def addVertex(self,vertex):
		if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True 
		else:
			return False 

	def addEdge(self,u,v,weight):
		#weight is the distance between two vertices
		#u and v are the names of the vertices 
		if u in self.vertices and v in self.vertices:
			self.vertices[u].addNeighbour(v,weight)
			self.vertices[v].addNeighbour(u,weight)
			return True
		else:
			return False 

	def resetGraph(self):
		#Resets the graph after applying an algorithm 
		for v in self.vertices.keys():
			if self.vertices[v].color != 'Black':
				self.vertices[v].color = 'Black'
			self.vertices[v].distance = sys.maxsize

	def dfs(self,vertex):
		#Depth First Search 
		vertex.color = 'Red' #Mark as visited 
		for v in vertex.neighbours:
			if self.vertices[v].color == 'Black':
				self.dfs(self.vertices[v])
		vertex.color = 'Blue'

	def bfs(self,vertex):
		#Breadth first search used to find the shortest path
		vertex.distance = 0
		vertex.color = 'Red' #Mark as visited
		Q = list()
		for v in vertex.neighbours:
			Q.append(v)
			self.vertices[v].distance = vertex.distance + vertex.neighbours[v]
		while len(Q):
			u = Q.pop(0) #Can be implemented with a heap data structure
			node_u = self.vertices[u]
			node_u.color = 'Red' #Mark as visited
			for v in node_u.neighbours:
				node_v = self.vertices[v]
				if node_v.color == 'Black':
					Q.append(v) #Rebuild the heap if unvisited 
					if node_v.distance > node_u.distance + node_u.neighbours[v]:
						node_v.distance = node_u.distance + node_u.neighbours[v]

def shortest(v,path):
	if v.previous:
		path.append(v.previous.name)
		shortest(v.previous,path)
	return 

def Djikstra(G,start):
	#Gets the shortest path from start to any vertex
	#This is together with the shortest() function written above
	#This is based on Breadth First search 
	start.distance = 0
	unvisitedQueue = [(G.vertices[v].distance,v) for v in G.vertices.keys()]
	heapq.heapify(unvisitedQueue)
	while len(unvisitedQueue):
		uv = heapq.heappop(unvisitedQueue)
		current = G.vertices[uv[1]]
		current.color = 'Red' #Mark as visited 
		for next in current.neighbours:
			if G.vertices[next].color == 'Red':
				continue #Go to the next vertex in the heap if this is already visited 
			newDist = current.distance + current.neighbours[next]
			if newDist < G.vertices[next].distance:
				G.vertices[next].distance = newDist
				G.vertices[next].previous = current #Set the previous vertex as the current vertex for the path
		while len(unvisitedQueue):
			heapq.heappop(unvisitedQueue) #pop every item
		#Rebuild the heap
		unvisitedQueue = [(G.vertices[v].distance,v) for v in G.vertices.keys()
								if G.vertices[v].color == 'Black']
		heapq.heapify(unvisitedQueue)




#Driving code for graph-based algorithms
#Uncomment to test
"""
g = Graph()
a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')
vertices = [a,b,c,d,e,f]
for vertex in vertices:
	g.addVertex(vertex)
g.addEdge('a', 'b', 7)  
g.addEdge('a', 'c', 9)
g.addEdge('a', 'f', 14)
g.addEdge('b', 'c', 10)
g.addEdge('b', 'd', 15)
g.addEdge('c', 'd', 11)
g.addEdge('c', 'f', 2)
g.addEdge('d', 'e', 6)
g.addEdge('e', 'f', 9)
for v in g.vertices:
	print(v)
	print(g.vertices[v].color)
	print(g.vertices[v].distance)
	print("\n")
print("After doing a Breadth-First Search from Vertex A:")
g.bfs(a)
for v in g.vertices:
	print(v)
	print(g.vertices[v].color)
	print(g.vertices[v].distance)
	print("\n")
#Reset the graph
g.resetGraph()
#Get the shortest path from a to d
path = ['d'] #Rebuild from the end. 
Djikstra(g,a)
shortest(d,path)
print(path)
"""

