import random
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def dfs_traversal(self):
        visited = set()
        res = []
        def dfs(node, visited, res):

            if node not in visited:
                res.append(node)
                #print(res)
                visited.add(node)
                for adj_node in self.adj_list[node]:
                    res = dfs(adj_node, visited, res)
            
            return res
        # Starting with any random node
        node = random.choice(list(self.adj_list.keys()))
        return(dfs(node, visited, res))

    def bfs_traversal(self):
        visited = set()
        res = []
        # Pickup any starting node
        node = random.choice(list(self.adj_list.keys()))

        queue = [node]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                res.append(node)
                visited.add(node)
                for adj_node in self.adj_list[node]:
                    queue.append(adj_node)
        return res

my_graph = Graph()
my_graph.add_vertex(0)
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)

my_graph.add_edge(0,1)
my_graph.add_edge(0,2)
my_graph.add_edge(0,3)

my_graph.add_edge(2,3)
my_graph.add_edge(2,4)


print('\nGraph Adjacency List Representation:')
my_graph.print_graph()

print('\nGraph DFS Traversal:')
print(my_graph.dfs_traversal())

print('\nGraph BFS Traversal:')
print(my_graph.bfs_traversal())