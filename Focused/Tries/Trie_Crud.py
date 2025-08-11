class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for c in word:
            # For each character in the word, if it's not a child of the
            # current node, create a new TrieNode for that character
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # Mark the last node as the end of a word
        node.is_word = True

    def search(self, word):
        node = self.root
        for c in word:
            # For each charater in the word, if its not a child of the
            # current node, the word does not exists in the trie
            if c not in node.children:
                return False
            node = node.children[c]
        # REturn whether the current node is marked as the end of the word
        return node.is_word
    
    def has_prefix(self, prefix):
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
        node = node.children[c]
        # Once we've traversed the nodes corresponding to each character in the prefix, 
        # return True
        return True
            
trie = Trie()

trie.insert("internet")
trie.insert("interface")
word = 'interface'
prefix = 'inter'
print(f"\nDoes trie has {word}? {trie.search(word)}\n")
print(f"\nDoes trie has {prefix}? {trie.has_prefix(prefix)}\n")