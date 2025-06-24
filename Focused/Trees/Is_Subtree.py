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
    
    def match_tree(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        
        if t1 is None and t2:
            return False
        
        if t2 is None and t1:
            return True
        
        return t1.value == t2.value and self.match_tree(t1.left, t2.left) and self.match_tree(t1.right, t2.right)
    
    def is_subtree(self, t1, t2):
        if t2 is None:
            return True
        if t1 is None:
            return False
        
        if t1.value == t2.value:
            return (self.match_tree(t1, t2))
        
        return (self.is_subtree(t1.left, t2) | self.is_subtree(t1.right, t2))

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

my_tree1 = BinarySearchTree()
my_tree1.insert(2)
my_tree1.insert(3)
my_tree1.insert(1)
my_tree1.insert(4)
#my_tree1.insert(5)


print("\n")
my_tree.print_tree(my_tree.root, 0, "t1: ")
my_tree1.print_tree(my_tree1.root, 0, "t2: ")

print("\n")
print(f"Does T2 a sub-tree of a T1? {my_tree.is_subtree(my_tree.root, my_tree1.root) if my_tree is not None else False}")
print("\n")
