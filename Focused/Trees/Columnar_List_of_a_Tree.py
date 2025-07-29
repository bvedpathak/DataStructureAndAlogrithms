class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_tree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left is not None or root.right is not None:
                self.print_tree(root.left, level + 1, "L--- ")
                self.print_tree(root.right, level + 1, "R--- ")

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while temp:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
                continue
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
        return True
    
# The logic is simple, curr_index at the root is at 0 and everytime you move left
# decrement it by 1 and everytime you move right, increment it by 1. Maintain a hashmap
# of the values for the respective column and then flatten the hashmap to a list at the 
# end before returning. I solved it using DFS but you can also solve using BFS traversal
# Time: O(n) and Space: O(n)

def columnar_list(root):
    res = []
    min_index, max_index = 0, 0

    # The actual DFS function to traverse and collect columnar elements
    def traverse_and_collect(root, curr_index, lookup):
        if not root:
            return lookup
        
        nonlocal min_index, max_index

        # Add the current value to the corresponding column index 
        lst = lookup.get(curr_index, [])
        lst.append(root.value)
        lookup[curr_index] = lst
        min_index = min(min_index, curr_index)
        max_index = max(max_index, curr_index)
        # Do a DFS and repeat..at the end return the hashmap 
        lookup = traverse_and_collect(root.left, curr_index - 1, lookup)
        return(traverse_and_collect(root.right, curr_index + 1, lookup))
    
    # Call the subfunction
    lookup = traverse_and_collect(root, 0, {})

    # Now we need to flatten the hashamp into a list. Since column ids can be negative, 
    # we in-place create a list by sequencially traversing from min_index to max_index
    return [lookup.get(i, []) for i in range(min_index, max_index + 1)]


my_tree = BinarySearchTree()
my_tree.insert(5)
my_tree.insert(2)
my_tree.insert(7)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(7)
my_tree.insert(8)

print("\n")
my_tree.print_tree(my_tree.root, 0, "root: ")

print("\n")
print(f"{columnar_list(my_tree.root)}")
print("\n")
