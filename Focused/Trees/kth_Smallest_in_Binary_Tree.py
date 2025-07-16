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
    
    def kth_smallest(self, curr_node, count, k):
        ans_node = None
        
        def find_kth_smallest(curr_node, count, k):
            nonlocal ans_node
            if count >= k:
                return count
            
            if curr_node is None:
                #count += 0
                return count
            
            count = find_kth_smallest(curr_node.left, count, k)
            count += 1
            
            if count == k:
                ans_node = curr_node
                return count
            
            count = find_kth_smallest(curr_node.right, count, k)
            return count
        
        find_kth_smallest(curr_node, count, k)
        return ans_node.value if ans_node is not None else None

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


k = 7
my_tree.print_tree(my_tree.root, 0, "Root: ")

print(f"The {k}th smallest in the Tree is: {my_tree.kth_smallest(my_tree.root, 0, k)}")





