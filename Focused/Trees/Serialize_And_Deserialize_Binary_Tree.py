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
    
    def serialize_binary_tree(self, curr_node, val):
        if curr_node is None:
            val += "X#"
            return val
        
        val += str(curr_node.value) + "#"

        val = self.serialize_binary_tree(curr_node.left, val)
        val = self.serialize_binary_tree(curr_node.right, val)
        return val

    def deserialize_binary_tree(self, val):
        queue = val.split("#")
        def deserialize(queue):
            if queue is None or len(queue) < 1:
                return None
            node_val = queue.pop(0)
            
            if node_val == 'X':
                return None
            
            node = Node(node_val)
            node.left = deserialize(queue)
            node.right = deserialize(queue)
            return node
        
        return(deserialize(queue))

        
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(5)
my_tree.insert(6)
   
print(f"The serialized version the Tree is: {my_tree.serialize_binary_tree(my_tree.root, "") if my_tree is not None else "X#"}")

my_tree.print_tree(my_tree.root, 0, "Root: ")
start = my_tree.deserialize_binary_tree("2#1#X#X#3#X#4#X#5#X#X#")
my_tree.print_tree(start, 0, "Root: ")
