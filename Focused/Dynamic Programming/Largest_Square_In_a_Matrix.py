# Determine the area of the largest square of 1's in a binary matrix.
# Time: O(m.n) Space: O(m.n)
def largest_square_in_a_matrix(matrix):
    if not matrix:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    max_len = 0

    # Base case: If a cell in a row 0 is 1, the largest square there has 
    # a length of 1
    for j in range(n):
        if matrix[0][j] == 1:
            dp[0][1] = 1
            max_len = 1
    
    # Base case: If a cell in column 0  is 1, the largest square ending 
    # there has a length of 1
    for i in range(m):
        if matrix[i][0] == 1:
            dp[i][0] = 1
            max_len = 1
    
    # Populate the rest of the DP table and keep track of max_len
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                # The length of the largest square ending here is determined by
                # the smallest square ending at the neighboring cells (left, top-left, top)
                # plus 1 to include this cell
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
                # Maintain the max len see so far
                max_len = max(max_len, dp[i][j])
    
    return max_len ** 2

# Since we only need a reference of one previous row, we can optimize the space even further
# Time: O(m.n) Space: O(n)
def largest_square_in_a_matrix_optimized(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    max_len = 0
    prev_row = [0 for _ in range(n)]

    # Base case: If a cell in a row 0 is 1, the largest square there has 
    # a length of 1
    for j in range(n):
        if prev_row[j] == 1:
            prev_row[j] = 1
            max_len = 1
    # Iterate thru the input and populate
    for i in range(1, m):
        curr_row = [0 for _ in range(n)]
        # Base cases: if current row's 0th element is 1, then mark it accordingly
        curr_row[0] = matrix[i][0]
        max_len = max(max_len, curr_row[0])
        for j in range(1, n):
            if matrix[i][j] == 1:
                # curr_row[j] = 1 + min(left, top-left, top)
                curr_row[j] = 1 + min(curr_row[j - 1], prev_row[j-1], prev_row[j])
                # Maintain the max len so far
                max_len = max(max_len, curr_row[j])
        # This one is important, to make prev as curr for the next iteration
        prev_row = curr_row
    return max_len ** 2

matrix = [[1, 0, 1, 1, 0],
          [0, 0, 1, 1, 1],
          [1, 1, 1, 1, 0],
          [1, 1, 1, 0, 1],
          [1, 1, 1, 0, 1]
          ]

print(f"\nLargest Square in the given Matrix is: {largest_square_in_a_matrix(matrix)}\n")
print(f"\nLargest Square in the given Matrix is: {largest_square_in_a_matrix_optimized(matrix)}\n")