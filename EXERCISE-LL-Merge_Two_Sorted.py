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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def add_new_node(self, prev, node):
        if node is None:
            return
        new_node = Node(node.value)
        if prev is None:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return

    def merge(self, list1):
        prev = None
        curr = self.head
        new_list_curr = list1.head
        while curr is not None:
            while new_list_curr is not None:
                if new_list_curr.value <= curr.value:
                    self.add_new_node(prev, new_list_curr)
                else:
                    break
                new_list_curr = new_list_curr.next
            if new_list_curr is None:
                return
            prev = curr
            curr = curr.next

        while new_list_curr is not None:
            self.add_new_node(prev, new_list_curr)
            prev = prev.next
            new_list_curr = new_list_curr.next

        self.tail = prev

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""