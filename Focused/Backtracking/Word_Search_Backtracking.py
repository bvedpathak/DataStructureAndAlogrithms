def does_adjacent_match(board, i, j, word, index):
    if i >= len(board) or i < 0:
        return False
    if j >= len(board[i]) or j < 0:
        return False
    if index >= len(word):
        return True
    if board[i][j] == word[index]:
        if does_adjacent_match(board, i+1, j, word, index+1) or \
           does_adjacent_match(board, i-1, j, word, index+1) or \
           does_adjacent_match(board, i, j+1, word, index+1) or \
           does_adjacent_match(board, i, j-1, word, index+1):
            return True
        
    return False

    
def adjacent_word_search(board, word):
    if word is None or len(word) < 0:
        return True
    
    if board is None or len(board) < 0:
        return False
    
    index = 0
    # Below code snippet is to find the starting match
    # and then ask the recurrsive fuction to match adjacent letters
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[index]:
               if does_adjacent_match(board, i, j, word, index):
                   return True
    return False

board = [
    ['A', 'B', 'C', 'D'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
]
word = "SAD"
print("\n\n")
print(f"Does {word} present in board? {adjacent_word_search(board, word)}")
print("\n\n")
