## The intution method of traversing thru all the elements
## and maintaining a set of row/column to be zerod out and then 
## zeroing them out in the second pass
## Time: O(n2), Space: O(n)
def zero_out_row_and_column_v1(matrix):
    if matrix is None:
        return None

    column_set = set()
    row_set = set()
 
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if matrix[i][j] == 0:
                row_set.add(i)
                column_set.add(j)

    ## Zero out rows
    for i in row_set:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0

    ## Zero out Cols
    for i in range(len(matrix)):
        for j in column_set:
            matrix[i][j] = 0
    return matrix

## A better approach without using an extra space. The idea is instead of maintain
## a row set and a col set, we will re-use the row[0] and col[0] to maintain this
## information (we can call this as a bubbling up zeros). We also need to use flags
## to know if whether the row[0] and col[0] had any organic zeros to begin with and
## zero the entire row[0] or col[0] at the very last
## Time: O(n2), Space: O(1)
def zero_out_row_and_column_v2(matrix):
    if matrix is None:
        return None
    
    if len(matrix) < 1:
        return matrix
    
    row_has_zero = False
    col_has_zero = False

    ## check first for the oganic zeros in at any place in row 0
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            row_has_zero = True

    ## check first for the oganic zeros in at any place in row 0
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            col_has_zero = True

    ## Traverse thru the remaining matrix and "Bubble Up" the zeros 
    ## to the respective rows and columns
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                ## Buble up the zeros to row 0
                matrix[0][j] = 0
                ## Buble up the zeros to col 0
                matrix[i][0] = 0
    ## Traverse thru the matrix and zero out entire rows/cols based on
    ## what row 0 and col 0 says (where we bubbled up the zeros)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ## if row 0 col 0 shows it was zero then zero it out
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    ## Now set the entire row 0 to zero if there was an organic zero
    if row_has_zero:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    
    ## Now set the entire col 0 to zero if there was an organic zero
    if col_has_zero:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    return matrix

print("\n")
matrix =[[ 1,  2,  3,  4],
         [ 5,  9,  7,  8],
         [ 9, 10,  0, 12],
         [13, 14, 15, 16]
         ]

matrix1 =[[ 1,  2,  3,  4],
         [ 5,  6,  7,  8],
         [ 9, 10, 11, 12]
         ]

matrix2 =[[ 1,  2],
         [ 5,  6]
         ]

#for i in zero_out_row_and_column_v1(matrix):
#    print(i)

print("\n")
for i in zero_out_row_and_column_v2(matrix):
    print(i)
