# A graph is bipartite if the nodes ca be colored in one of the two colors,
# so that no two adjacent nodes are the same color.
# Solution is to do a DFS and maintain color for each node and while doing that
# if we come across a case where two adjacent nodes appear to be same color, 
# we return False and declare that the graph is not bipartite
# Time: O(m .n) Space: O(n) to maintain color list (this list is same as visited)

def bipartite_graph_validaion(graph):
    if not graph:
        return True
    
    colors = [0 for _ in range(len(graph))]
    
    # Determine if each graph component is bipartite
    for i in range(len(graph)):
        if colors[i] == 0 and not dfs(i, 1, colors, graph):
            return False
   
    return True

def dfs(node, color, colors, graph):
    if node >= len(graph):
        return False
    colors[node] = color

    for neighbor in graph[node]:
        # If the current neighbor has the same color as the current node,
        # then the graph is not bipartite
        if colors[neighbor] == color:
            return False
        
        # if the current neighbor is not colored, color it with the other 
        # color (i.e. -color) and continue the DFS
        if colors[neighbor] == 0 and not dfs(neighbor, -color, colors, graph):
            return False
    return True
    
print("\n")

graph = [[1,4], [0, 2], [1], [4], [0, 3]]

print(f"The graph {graph} is bipartite? {bipartite_graph_validaion(graph)}")


