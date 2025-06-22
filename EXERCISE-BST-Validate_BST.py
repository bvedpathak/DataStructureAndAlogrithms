class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def right_insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

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
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def is_valid_bst(self):
        def __is_valid_bst(current_node, parent):
            if current_node is None:
                return True
            left_valid = __is_valid_bst(current_node.left, current_node)
            print(current_node.value)
            right_valid = __is_valid_bst(current_node.right, current_node)

            if not left_valid or not right_valid:
                return False

            if parent is not None:
                if parent.left is not None:
                    if parent.left.value > parent.value:
                        return False
                if parent.right is not None:
                    if parent.right.value < parent.value:
                        return False
            return True
        return __is_valid_bst(self.root, None)

    ## This was an initial intuition one and does NOT cover a few corner cases 
    ## so just for reference and not to use in Production
    def validate_bst(self, root):
        if root is None:
            return True
        
        if root.left is not None and root.left.value > root.value or root.right is not None and root.right.value < root.value:
            return False

        return self.validate_bst(root.left) and self.validate_bst(root.right)
    
    ## This one is the optimized one and covers all the cases
    def validate_bst_v2(self, root, min_val, max_val):
        if root is None:
            return True
        
        if min_val > root.value or max_val < root.value:
            return False
                
        return self.validate_bst_v2(root.left, min_val, root.value) and self.validate_bst_v2(root.right, root.value, max_val)
        
    
my_tree = BinarySearchTree()
my_tree.right_insert(7)
my_tree.right_insert(2)
my_tree.right_insert(8)
my_tree.right_insert(4)
my_tree.right_insert(5)
my_tree.right_insert(5)

print(my_tree.print_tree(my_tree.root))
print("First BST is valid:")
print(my_tree.is_valid_bst())
print(my_tree.validate_bst(my_tree.root))
print(my_tree.validate_bst_v2(my_tree.root, float('-inf'), float('inf')))

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.print_tree(my_tree.root))
print("Second BST is valid:")
print(my_tree.is_valid_bst())
print(my_tree.validate_bst(my_tree.root))
print(my_tree.validate_bst_v2(my_tree.root, float('-inf'), float('inf')))

"""
    EXPECTED OUTPUT:
    ----------------
    BST is valid:
    True

 """