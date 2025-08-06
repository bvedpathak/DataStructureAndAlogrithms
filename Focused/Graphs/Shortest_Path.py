# Given an integer n representing nodes labeled from 0 to n - 1 in an undirected graph,
# and an array of non-negative weighted edges, return an array where each index i contains
# the shortest path length from a specified start node to node i. If a node is unreachable,
# set its distance to -1

# Each edge is represented by a triplet of positive integers: the start node, the end node
# set the weight of the edge
# Time: O(n.e) Space: O(n) 
# Below is one way to solve it but you can also solve using Min_Heap to make it more efficient

from collections import deque, defaultdict

def shortest_path(start, no_of_vertices, edges):
    if not edges or no_of_vertices < 1 or start >= no_of_vertices:
        return None
    # This is the result list that will be returned
    dist = [ -1 for _ in range(no_of_vertices)]
    visited = set()
    graph = defaultdict(list)
    queue = deque()
    # Go thru the edges and form a graph as an adjacency list
    for v, n, d in edges:
        graph[v].append((n, d))
        # Since the graph is bi-directional, also add a reverse edge
        graph[n].append((v, d))
    # Start with 'start' vertex by adding in the queue
    queue.append(start)
    # Distance from start to start is always zero so record that
    dist[start] = 0 
    # Perform the BFS traversal and record the shortest path seen
    while queue:
        curr = queue.popleft()
        # Skip if we already visited a vertex
        if curr is visited:
            continue
        curr_dist = dist[curr]
        # Go thru all the neighbors 'n' and the distances 'd'
        for n, d in graph.get(curr, []):
            # Record the shortest path i.e. min betwee
            # 1. curr_dist i.e. current distance plus the 'd'
            # 2. Already seen distance for this node from any other node 
            # as recorded previously in dist[n]
            dist[n] = min(dist[n], curr_dist + d) if dist[n] != -1 else curr_dist + d
            # If we have not not performed BFS yet on this node then go on
            # else skip and pop the next from the queue
            if n not in visited:
                queue.append(n)
        # Mark visited so that we wont keep visiting nodes in cycle
        visited.add(curr)
    return dist

no_of_vertices = 6
start = 0
# Format [Vertex, Next_Vertex, Distance between the Vertex]
edges = [[0, 1, 5], [0, 2, 3], [1, 2, 1], [1, 3, 4], [2, 3, 4], [2, 4, 5]]
# Output Format
# [(index represents vertex) and the number at the index is the shortest distance \
# from the start vertex]
print(f"Shorted distance from the node {start} to all other rechable node is: \
      {shortest_path(start, no_of_vertices, edges)}")

