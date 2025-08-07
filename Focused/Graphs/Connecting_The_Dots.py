# Given a set of points on a plane, determine the minimum cost to connect all these points.
# The cost of connecting two points is equal to the Manhattan distance between them, which is
# calculated as |x1-x2|+|y1-y2| for two points (x1, y1) and (x2, y2).
# The goal is to connect all nodes (points) in such a way that the total cost is minimized. 
# This is essentially the minimum spanning tree (MST) problem:
# There are two main algorithms that are used to find the MST of a graph:
# Kruskal's algorithm
# Prim's algorithm

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]
            # Return True if both groups were merged.
            return True
        # Return False if the points belong to the same group.
        return False
    
    def find(self, x) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

def connect_the_dots(points):
    n = len(points)
    # Create and populate an array containing all possible edges.
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            # Manhattan distance.
            cost = (abs(points[i][0] - points[j][0]) +
                    abs(points[i][1] - points[j][1]))
            edges.append((cost, i, j))
    # Sort the edges by their cost in ascending order.
    edges.sort()
    uf = UnionFind(n)
    total_cost = edges_added = 0
    # Use Kruskal's algorithm to create the MST and identify its minimum cost.
    for cost, p1, p2 in edges:
        # If the points are not already connected (i.e., their representatives are
        # not the same), connect them, and add the cost to the total cost.
        if uf.union(p1, p2):
            total_cost += cost
            edges_added += 1
            # If n - 1 edges have been added to the MST, the MST is complete.
            if edges_added == n - 1:
                return total_cost
     
points = [[1, 1], [2, 6], [3, 2], [4, 3], [7, 1]]

print(f"\nAll dots can be connected with the minimum weight of: {connect_the_dots(points)}\n")