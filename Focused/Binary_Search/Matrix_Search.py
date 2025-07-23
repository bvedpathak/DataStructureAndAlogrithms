def matrix_search(matrix, target):
    if not matrix:
        return [-1, -1]
    
    row_max, col_max = len(matrix), len(matrix[0])

    l , r = 0, row_max * col_max

    while l < r:
        mid = (l + r) // 2

        # This is the main change to map the l and r to the row and col
        # Otherwise the rest is the typical binary search
        row, col = mid // col_max, mid % col_max

        if matrix[row][col] == target:
            return [row, col]
        
        if matrix[row][col] > target:
            r = mid 
        else:
            l = mid + 1
    return [-1, -1]


print("\n")
matrix = [[ 2,  3,  4,  6],
          [ 7, 10, 11, 17],
          [20, 21, 24, 33]
          ]
target = 3

print(f"Index at which {target} is present in the matrix: {matrix_search(matrix, target)} ")