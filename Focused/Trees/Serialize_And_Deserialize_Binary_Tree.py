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
    
    def serialize_binary_tree(self, curr_node, val):
        if curr_node is None:
            val += "X#"
            return val
        
        val += str(curr_node.value) + "#"

        val = self.serialize_binary_tree(curr_node.left, val)
        val = self.serialize_binary_tree(curr_node.right, val)
        return val

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(5)
   
print(f"The serialized version the Tree is: {my_tree.serialize_binary_tree(my_tree.root, "") if my_tree is not None else "X#"}")



