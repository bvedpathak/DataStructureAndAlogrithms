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

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length += 1


"""
def find_kth_from_end(ll, k):
    if ll.head is None:
        return None

    temp = ll.head
    k_element = None
    counter = 0
    flag = False
    while temp is not None:
        temp = temp.next
        if counter % k == 0 and flag is False:
            if k_element is None:
                k_element = ll.head
                flag = True
        elif flag is True:
            k_element = k_element.next
        counter += 1
    return k_element
"""

def find_kth_from_end(ll, k):
    if ll.head is None:
        return None

    temp = ll.head
    k_element = ll.head
    counter = 1
    while temp.next is not None:
        temp = temp.next
        if counter >= k:
            k_element = k_element.next
        counter += 1

    if counter >= k:
        return k_element
    else:
        return None

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

k = 1
result = find_kth_from_end(my_linked_list, k)
if result is None:
    print("Result is None")
else:
    print(result.value)  # Output: 4

"""
my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()
"""

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2

"""
