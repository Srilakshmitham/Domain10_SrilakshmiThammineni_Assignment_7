from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for neighbor in self.graph[v]:
        
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            
            elif neighbor != parent:
                return True

        return False

    def is_cyclic(self):
        visited = {node: False for node in self.graph}

        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, -1):
                    return True
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)   

print("Graph contains cycle:" if g.is_cyclic() else "No cycle found.")
