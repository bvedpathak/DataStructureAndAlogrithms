class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

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
    
    def is_symmetric(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None and t2 or t1 and t2 is None:
            return False
        
        return t1.value == t2.value and self.is_symmetric(t1.left, t2.right) and self.is_symmetric(t1.right, t2.left)
    
    def depth_of_binary_tree(self, curr_node):
        if curr_node is None:
            return 0
        if curr_node.left is None and curr_node.right is None:
            return 1
        return(max(self.depth_of_binary_tree(curr_node.left), self.depth_of_binary_tree(curr_node.right))+1)

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(5)
   
print(f"The max depth of the Tree is: {my_tree.depth_of_binary_tree(my_tree.root) if my_tree is not None else 0}")

