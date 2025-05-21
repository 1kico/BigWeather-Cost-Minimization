# Same as initial code but adding the brute-force approach to satisfy the Bonus Considerations.

# Graph Class
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in range(n + 1)]

    def add_pair(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def get_neighbors(self, node):
        return self.adj[node]

# Queue Class
class Queue:
    def __init__(self):
        self.items = []
        self.start = 0

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
file_path = input("Enter absolute path to input file: ").strip()
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

n, k, bucket_cost, bond_cost = map(int, lines[0].split())
graph = Graph(n)

for line in lines[1:]:
    u, v = map(int, line.split())
    graph.add_pair(u, v)

visited = [False] * (n + 1)



# BFS
def bfs(start):
    queue = Queue()
    queue.enqueue(start)
    component = []
    visited[start] = True

    while not queue.is_empty():
        node = queue.dequeue()
        component.append(node)
        for neighbor in graph.get_neighbors(node):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.enqueue(neighbor)
    return component


total_cost = 0
total_configurations = 1
components_best_hosts = []

# Brute-force 
def count_brute_force(component, graph, bucket_cost, bond_cost): # Brute-force function to find the minimum cost and configurations
    def is_valid(hosts): # Check if the selected hosts are valid
        host_set = set(hosts) # Convert list to set for faster lookup
        for node in component: # Check each node in the component
            if node in host_set: # If the node is a host, skip it
                continue
            neighbors = graph.get_neighbors(node) 
            if not any(neigh in host_set for neigh in neighbors): # If no neighbor is a host, it's invalid
                return False
        return True

    n = len(component) # Number of nodes in the component
    min_cost = float('inf') # Initialize minimum cost to infinity as default vaule
    count = 0 # Count of configurations
    best_hosts = [] # List to store the best hosts

    for i in range(1, 2 ** n): #Iterates using bitmasking
        hosts = [] 
        for j in range(n): # Check each bit
            if (i >> j) & 1: # If the j-th bit is set, include the corresponding node
                hosts.append(component[j]) 

        if not is_valid(hosts): # If the selected hosts are not valid, skip
            continue

        bond_count = 0 #Initialize bond count in oreder to calculate the cost
        for node in component:
            if node in hosts:
                continue
            for neigh in graph.get_neighbors(node): 
                if neigh in hosts: # If the neighbor is a host, count it as a bond
                    bond_count += 1
                    break

        cost = len(hosts) * bucket_cost + bond_count * bond_cost # Calculate the total cost

        if cost < min_cost: # If the cost is less than the minimum cost found so far
            min_cost = cost # Update the minimum cost
            count = 1 # Reset the count to 1
            best_hosts = hosts # Update the best hosts
        elif cost == min_cost: # If the cost is equal to the minimum cost
            count += 1 # Increment the count

    if count == 0: # If no valid configuration is found, return the cost of using only buckets
        return len(component) * bucket_cost 
    return min_cost, count, best_hosts 



# Process each connected component
for node in range(1, n + 1):
    if not visited[node]:
        component = bfs(node)
        cost, ways, best_hosts = count_brute_force(component, graph, bucket_cost, bond_cost)
        total_cost += cost
        total_configurations *= ways
        components_best_hosts.append((component, best_hosts))

# Output
print("\nCheapest", total_cost)
print("Number of cheapest configurations:", total_configurations)
print("\nOne cheapest solution (bucket placements):")
for component, best_hosts in components_best_hosts:
    print(f"Component {component}: Buckets on {sorted(best_hosts)}")