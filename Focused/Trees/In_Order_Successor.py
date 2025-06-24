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
    
    ## This is still a work in progress...
    def find_in_order_successor(self, root, target, ans_node, parent):
        if root is None:
            return None
                
        if root.right is not None and root.right.value == target:
            ans_node = root.right
            return ans_node
        
        if ans_node is not None:
            return ans_node
        '''
        if ans_node is not None and parent is not None and parent.value == target:
            return ans_node
        '''
        ans_node = self.find_in_order_successor(root.left, target, ans_node, root)
        if root is not None and root.value == target:
            ans_node = root.right
            return ans_node
        ans_node = self.find_in_order_successor(root.right, target, ans_node, root)

        return ans_node
    
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
print("\n")
target = 4
ans_node = my_tree.find_in_order_successor(my_tree.root, target, None, None)
print(f"In order successor for {target} is: {ans_node.value if ans_node is not None else None}")
print("\n")