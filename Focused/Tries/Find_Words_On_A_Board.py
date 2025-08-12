class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def find_all_words_on_a_board(board, words):
    root = TrieNode()
    # Insert every word into the trie.
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    res = []
    # Start a DFS call from each cell of the board that contains a 
    # child of the root node, which represents the first letter of a 
    # word in the trie
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in root.children:
                dfs(board, r, c, root.children[board[r][c]], res)
    return res

def dfs(board, r, c, node, res):
    if node.word:
        res.append(node.word)
    
    temp = board[r][c]
    # Mark the current cell as visisted
    board[r][c] = '#'
    # Explore all adjacent cells that correspond with a child of the
    # current TrieNode
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in dirs:
        next_r, next_c = r + d[0], c + d[1]
        if (is_within_bounds(next_r, next_c, board)
            and board[next_r][next_c] in node.children):
            dfs(
                board, next_r, next_c, node.children[board[next_r][next_c]],
                res
            )
    # Backgrack the reverting the cell back to its original character
    board[r][c] = temp

    def is_within_bounds(r, c, board):
        return 0 <= r < len(board) and 0 <= c < len(board[0])
    '''
    board = [['b', 'y', 's'],
             ['b', 'y', 's'],
             ['b', 'y', 's']
             
'''