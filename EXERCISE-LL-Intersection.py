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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def is_intersection(self, lst1, lst2):
        if lst1 is None or lst2 is None:
            return None
        curr1 = lst1.head
        curr2 = lst2.head

        while curr1 != curr2:
            curr1 = curr1.next if curr1 else lst2.head
            curr2 = curr2.next if curr2 else lst1.head

        return curr1

my_linked_list1 = LinkedList(0)
my_linked_list1.append(2)
my_linked_list1.append(3)

my_linked_list = LinkedList(1)
my_linked_list.append(4)

## Append the tail to intersect
my_linked_list1.tail.next = my_linked_list.tail
my_linked_list1.tail = my_linked_list1.tail.next
my_linked_list1.length += 1

my_linked_list.append(7)

my_linked_list1.tail.next = my_linked_list.tail
my_linked_list1.tail = my_linked_list1.tail.next
my_linked_list1.length += 1

my_linked_list.append(8)
my_linked_list1.tail.next = my_linked_list.tail
my_linked_list1.tail = my_linked_list1.tail.next
my_linked_list1.length += 1

my_linked_list.append(9)
my_linked_list1.tail.next = my_linked_list.tail
my_linked_list1.tail = my_linked_list1.tail.next
my_linked_list1.length += 1


print('LL before reverse():')
my_linked_list.print_list()

print('\nLL after reverse():')
my_linked_list1.print_list()

print(f"Does two list intersect? {my_linked_list.is_intersection(my_linked_list, my_linked_list1).value}")

"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1

"""