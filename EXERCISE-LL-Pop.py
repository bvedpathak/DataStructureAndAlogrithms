class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        tail_node = self.tail
        if self.length == 0:
            return None

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next:
                if temp.next == self.tail:
                    self.tail = temp
                    self.tail.next = None
                else:
                    temp = temp.next
        self.length -= 1
        return tail_node

    
my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""