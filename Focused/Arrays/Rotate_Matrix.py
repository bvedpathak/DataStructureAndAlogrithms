## The intution method of traversing thru all the elements
## and adding them to a right place in the new matrix
## Time: O(n2), Space: O(n)
def rotate_matrix_v1(matrix):
    if matrix is None:
        return None
    if len(matrix) < 1:
        return matrix
    
    row_max = len(matrix)
    col_max = len(matrix[0])    

    result = [[0 for _ in range(row_max)] for _ in range(col_max)]

    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            place = row_max - 1 - i
            result[j][place] = matrix[i][j]
    
    return result

## A better approach without using an extra space
## Time: O(n2), Space: O(1)
## Constraint: Since it is a in-place replacement, the M X N should be the same
def rotate_matrix_v2(matrix):
    if matrix is None:
        return None
    if len(matrix) < 1:
        return matrix
    row_max = len(matrix)
    col_max = len(matrix[0])  
    for i in range(col_max//2):
        for j in range(i, col_max - 1):
            count = 0
            temp = matrix[i][j]
            ## Only 4 sides to move so this look has to be a constant
            while count < 4:
                temp1 = matrix[j][row_max - 1 - i]
                matrix[j][row_max - 1 - i] = temp
                temp = temp1
                temp_i = i
                i = j
                j = row_max - 1 - temp_i
                count += 1
    return matrix

print("\n")
matrix =[[ 1,  2,  3,  4],
         [ 5,  6,  7,  8],
         [ 9, 10, 11, 12],
         [13, 14, 15, 16]
         ]

matrix1 =[[ 1,  2,  3,  4],
         [ 5,  6,  7,  8],
         [ 9, 10, 11, 12]
         ]

matrix2 =[[ 1,  2],
         [ 5,  6]
         ]
for i in rotate_matrix_v2(matrix2):
    print(i)
