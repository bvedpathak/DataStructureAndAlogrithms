class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

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
    

    def zig_zag_level_traversal(self, root):
        if root is None:
            return None
        
        results = []
        right_to_left = Stack()
        left_to_right = Stack()
        left_to_right.push(root)
        curr = left_to_right
        target = right_to_left

        while not curr.is_empty():
            node = curr.pop()

            if target == right_to_left:
                target.push(node.right) if node.right else None
                target.push(node.left) if node.left else None
            else:
                target.push(node.left) if node.left else None
                target.push(node.right) if node.right else None
            
            if curr.is_empty():
                if curr == right_to_left:
                    curr = left_to_right
                    target = right_to_left
                else:
                    curr = right_to_left
                    target = left_to_right
            
            results.append(node.value)
        
        return results
    
my_tree = BinarySearchTree()
my_tree.insert(7)
my_tree.insert(2)
my_tree.insert(11)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(3)
my_tree.insert(5)
my_tree.insert(9)
my_tree.insert(10)

my_tree.print_tree(my_tree.root, 0, "Root: ")

print(my_tree.zig_zag_level_traversal(my_tree.root))

