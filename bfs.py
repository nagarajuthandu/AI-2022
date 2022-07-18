from collections import defaultdict
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def printGraph(self): 
        print(dict(self.graph))
    # Function to print a BFS of graph 
    def bfs(self,node):
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            print (s, end = " ") 
            gr=dict(self.graph)
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
  
  
# Create a graph 
g = Graph() 
while True:
    choice = input("do you want to add element Y / N")
    if choice=="Y":
        parent=input("Enter parent node")
        child=input("Enter child node")
        g.addEdge(parent, child) 
        g.printGraph()
    else:
        break

print("Your updated Graph is")
g.printGraph()
 
start=input("Enter strating element for BFS")
print ("Following is Breadth First Traversal")
g.bfs(start)
