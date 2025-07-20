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
    
    def invert_tree(self, root):
        if root is None:
            return None
        
        root.right, root.left = self.invert_tree(root.left), self.invert_tree(root.right)
        return root

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
my_tree.print_tree(my_tree.invert_tree(my_tree.root))
print("\n")
