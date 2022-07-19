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
     # Set to keep track of visited nodes.

    def dfs(self,node):
        visited = []
        stack = []
        visited.append(node)
        stack.append(node)

        while stack:
            s = stack.pop() 
            print (s, end = " ") 
            
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)
  
  
  
# Create a graph 
print("Create a graph")
g = Graph() 
while True:
    choice = input("do you want to add element Y / N ")
    if choice=="Y" or choice=="y":
        parent=input("Enter parent node")
        child=input("Enter child node")
        g.addEdge(parent, child) 
        g.printGraph()
    elif choice=="N" or choice=="n":
        break
    else:
        print("please enter Y/N ")

print("Your updated Graph is")
g.printGraph()
 
start=input("Enter strating element for BFS")
print ("Following is Breadth First Traversal")
g.dfs(start)
