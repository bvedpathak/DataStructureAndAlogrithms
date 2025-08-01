# A matrix is given comprises of 1s, 0s and 2s where 1 uninfected and 0 means empty
# and 2 means infected. All 2s infect their adjacent uninfected neighbors (1s) every 
# second. Your task is to find how many seconds it needs to infect the entire matrix
# Solution: Treat the cluster of 2s as a graph and do the DFS visiting all 
# connected 1s (uninfected) and marking them 2 (infected). One successful traversal meaning 
# how many uninfected neigbors got infected. Scan thru the entire matrix and collect max of
# seconds needed to infect the entire island 
# Time: O(n2), Space: O(1) 

def count_infection_time(matrix):
    if not matrix:
        return 0
    
    max_seconds = 0
    max_count = 0

    # Go thru all cells and do a recurrsive call if a particular cell is infected
    # to identify and count how many more can be infected
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                max_seconds = max(max_seconds, dfs(i, j, matrix, 0, max_count))
    return max_seconds


def dfs(i, j, matrix, count, max_count):
    if not matrix:
        return count 
    
    # Increment count and mark infected only when the cell is 1 i.e. uninfected
    if matrix[i][j] == 1:
        # Mark infected
        matrix[i][j] = 2

        # Increment the current count and maintain the max count for this recurrsive call
        count += 1
        max_count = max(max_count, count)

    # Otherwise for all adjust horizontal and vertical neighbors, see if anyone
    # will get infected and recurrsively check
    if i + 1 < len(matrix) and matrix[i + 1][j] == 1:
        max_count = dfs(i + 1, j, matrix, count, max_count)
    
    if i - 1 >= 0 and matrix[i - 1][j] == 1:
        max_count = dfs(i - 1, j, matrix, count, max_count)

    if j + 1 < len(matrix[i]) and matrix[i][j + 1] == 1:
        max_count = dfs(i, j + 1, matrix, count, max_count)

    if j - 1 >= 0 and matrix[i][j - 1] == 1:
        max_count = dfs(i, j - 1, matrix, count, max_count)

    return max_count


print("\n")
matrix = [[1, 1, 1, 0],
          [0, 0, 2, 0],
          [0, 1, 0, 1],
          [2, 1, 1, 1]
          ]

print(f"The max time (in seconds) needed for the input {matrix} to be infected: {count_infection_time(matrix)}")

