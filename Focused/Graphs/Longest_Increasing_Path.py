# Find the longest strictly increasing path in a matrix of positive integers. 
# A path is a sequence of cells where each one is 4-directionally adjacent 
# up, down, left or right ot the previous one
# The main contraint here is 'strictly' which means no same elements are part
# of the max path. 
# Time: O(m.n), Space: O(n) 

def longest_increasing_path(matrix):
    if not matrix:
        return 0
    
    max_path = 0
    max_count = 0
    # We will use memoization to store already visited paths for each node
    mem = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Go thru all cells and do a recurrsive call for each cell calculating the 
    # max inceasing path from that node
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Get the max path for the current node
            max_path = max(max_path, dfs(i, j, matrix, 0, max_count, mem))

    # Printing Memoization table for reference
    print("Memoization table for reference:")
    for i in range(len(mem)):
        print(mem[i])

    return max_path


def dfs(i, j, matrix, count, max_count, mem):
    if not matrix:
        return count 

    # If path already calculated then use that. 
    # Note: Typical memoization technique
    if mem[i][j] != 0:
        max_count = max(max_count, count + mem[i][j])
        return max_count
        
    # Increment the current count and maintain the max count for this recurrsive call
    count += 1
    max_count = max(max_count, count)

    # Otherwise for all adjust horizontal and vertical neighbors, see if anyone
    # has greater than current node and recurrsively check further
    if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
        max_count = dfs(i + 1, j, matrix, count, max_count, mem)
    
    if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
        max_count = dfs(i - 1, j, matrix, count, max_count, mem)

    if j + 1 < len(matrix[i]) and matrix[i][j + 1] > matrix[i][j]:
        max_count = dfs(i, j + 1, matrix, count, max_count, mem)

    if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
        max_count = dfs(i, j - 1, matrix, count, max_count, mem)

    # Keep a track of max_count seen for the current node 
    # Since it is a forward looking count, 
    mem[i][j] = max_count - count + 1
    return max_count


print("\n")

matrix = [[1, 5, 8],
          [3, 4, 4],
          [7, 9, 2]
          ]


print(f"The longest increasing path for the input {matrix} is: {longest_increasing_path(matrix)}")

