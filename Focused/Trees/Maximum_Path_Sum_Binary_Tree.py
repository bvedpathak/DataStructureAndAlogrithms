class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.ans = 0

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
    
    def max_path_sum(self, curr_node):
        if curr_node is None:
            return 0
        
        left_sum = self.max_path_sum(curr_node.left)
        right_sum = self.max_path_sum(curr_node.right)

        ## Max for the one side plus the current node
        max_side = max(curr_node.value, max(left_sum, right_sum) + curr_node.value)
        ## Max for the current node plus both the sides 
        max_current = max(max_side, curr_node.value + left_sum + right_sum)
        ## Store if current + one side is bigger or current + both side is bigger to a global variable
        self.ans = max(self.ans, max_current)
        
        ## Important: just return the current side maximum the entire so far across is the tree is stored
        ## in the global variable 
        return max_side
            
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
   
print("\n\n")
print("The existing full tree is:")
my_tree.print_tree(my_tree.root, 0, "Root: ")
print("\n")
print(f"The max_path_sum for a one side is: {my_tree.max_path_sum(my_tree.root)} and entire tree is {my_tree.ans}")

