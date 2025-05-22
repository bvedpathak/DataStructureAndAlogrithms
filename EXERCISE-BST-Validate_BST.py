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


my_tree = BinarySearchTree()
my_tree.right_insert(1)
my_tree.right_insert(2)
my_tree.right_insert(3)
my_tree.right_insert(4)
my_tree.right_insert(5)

print("First BST is valid:")
print(my_tree.is_valid_bst())


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("Second BST is valid:")
print(my_tree.is_valid_bst())

"""
    EXPECTED OUTPUT:
    ----------------
    BST is valid:
    True

 """