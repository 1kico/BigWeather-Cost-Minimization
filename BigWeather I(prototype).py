#Graph Class 
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in range(n + 1)] #List of lists representing adjacent to the node

    def add_pair(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def get_neighbors(self, node):
        return self.adj[node]

# Queue Class
class Queue:
    def __init__(self):
        self.items = [] # List to store items in the queue
        self.start = 0 # Start index for dequeueing

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.start < len(self.items):
            item = self.items[self.start]
            self.start += 1
            return item
        return None

    def is_empty(self):
        return self.start >= len(self.items)

# Read input
file_path = input("Enter absolute path to input file: ")
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()] # Read lines from the file and remove empty lines

n, k, bucket_cost, bond_cost = map(int, lines[0].split()) #Turns the stings into integers
graph = Graph(n) #Initializes the graph

for line in lines[1:]:
    u, v = map(int, line.split())
    graph.add_pair(u, v) #Adds the pairs to the graph

visited = [False] * (n + 1) #creates a list of visited nodes where all are initially false


# BFS
def bfs(start): # BFS function to find connected components
    queue = Queue() 
    queue.enqueue(start)
    component = [] # List to store the component nodes
    visited[start] = True # Mark the start node as visited

    while not queue.is_empty(): # Dequeue nodes until the queue is empty
        node = queue.dequeue() 
        component.append(node) # Add the node to the component list

        for neighbor in graph.get_neighbors(node): # Get neighbors of the current node
            if not visited[neighbor]:   # If the neighbor is not visited
                visited[neighbor] = True #  Mark it as visited
                queue.enqueue(neighbor)  # Enqueue the neighbor for further exploration
    return component


total_cost = 0 # Track total cost
total_configurations = 1  # Track number of cheapest solutions

# Process each connected component
for node in range(1, n + 1):
    if not visited[node]:
        component = bfs(node)
        size = len(component)

        if bucket_cost <= bond_cost:
            # Give each dyno a bucket
            cost = size * bucket_cost
        else:
            # One bucket + bonds for the rest
            cost = bucket_cost + (size - 1) * bond_cost

        total_cost += cost

print("Cheapest configuration:", total_cost)

#Only works with complete/star graphs since the logic assumes that all nodes are neighbors/connected
