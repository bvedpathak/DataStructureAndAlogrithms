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
    
    def path_sum_exists(self, curr_sum, target):
        results = []
        if self.root is None:
            return False
        
        def traverse_and_calculate(current_node, curr_sum, target):
            nonlocal results 
            if current_node is None:
                return False
            
            if current_node.value == target:
                results = [current_node.value]
                return True
            
            if curr_sum == target:
                return True
            
            if curr_sum > target:
                results = []
                curr_sum = 0
            
            curr_sum += current_node.value
            results.append(current_node.value)

            return traverse_and_calculate(current_node.left, curr_sum, target) | traverse_and_calculate(current_node.right, curr_sum, target)

        ans = traverse_and_calculate(self.root, curr_sum, target)
        print(results)
        return ans
        


my_tree = BinarySearchTree()
my_tree.right_insert(1)
my_tree.right_insert(2)
my_tree.right_insert(3)
my_tree.right_insert(4)
my_tree.right_insert(5)

print("First BST is valid:")
print(my_tree.is_valid_bst())



print("\n\n")
#print(my_tree.dfs_in_order())
print(my_tree.path_sum_exists(0, 7))
print("\n\n")


"""
    EXPECTED OUTPUT:
    ----------------
    BST is valid:
    True

 """