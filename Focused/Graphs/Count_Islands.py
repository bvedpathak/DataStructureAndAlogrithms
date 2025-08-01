# A matrix is given comprises of 1s and 0s where 1 denotes land and 0 water
# your task is to return how many islands are there in the matrix. The island
# is defined as a bunch of 1s surrounded by either matrix boundaries or water 
# i.e. 0s. 
# Solution: Treat the cluster of 1s as a graph and do the DFS visiting all 
# connected 1s and marking them -1. One successful traversal meaning one island
# scan thru the entire matrix and collect all islands 
# Time: O(n2), Space: O(1) if input is not allowed to be changed then Space: O(n)

def count_islands(matrix):
    if not matrix:
        return 0
    no_of_islands = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                dfs(i, j, matrix)
                no_of_islands += 1
    return no_of_islands


def dfs(i, j, matrix):
    if not matrix:
        return 
    
    # Make sure i and j are within the bounds
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
        if matrix[i][j] == 1:
            # Mark visited (Assumption here is the input can be changed)
            # Otherwise we need to maitain a separate space to track
            # visited
            matrix[i][j] = -1
            # Visit the adjacent horizontal and vertical nodes and repeat the same
            dfs(i + 1, j, matrix)
            dfs(i, j + 1, matrix)
            dfs(i - 1, j, matrix)
            dfs(i, j - 1, matrix)
    return 


print("\n")
matrix = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 1]
          ]

print(f"No of islands in the input {matrix} are: {count_islands(matrix)}")

