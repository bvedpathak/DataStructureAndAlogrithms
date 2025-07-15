def is_sudoku_valid(board):
    if not board:
        return None
    
    rows = len(board)
    cols = len(board[0])
    grid_size = 3

    row_lookup = [ set() for _ in range(rows)]
    col_lookup = [ set() for _ in range(cols)]
    grid_lookup = [ [set() for _ in range(grid_size)] for _ in range(grid_size) ]    

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                continue

            # Check for duplicates in row lookup
            if board[i][j] in row_lookup[i]:
                return False
            row_lookup[i].add(board[i][j])

            # Check for duplicates in col lookup
            if board[i][j] in col_lookup[j]:
                return False
            col_lookup[j].add(board[i][j])

            # Check for duplicates in the grid lookup
            if board[i][j] in grid_lookup[i//grid_size][j//grid_size]:
                return False
            grid_lookup[i//grid_size][j//grid_size].add(board[i][j])

    return True


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0]
]
print("\n")
print(f"is Sudoku board valid? {is_sudoku_valid(board)}")
print("\n")
