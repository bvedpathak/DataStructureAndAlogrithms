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


    def swap(self, prev_curr, curr, prev_min, min):
        if curr == min or curr is None or min is None:
            return
        if min == self.tail:
            self.tail = curr

        if prev_curr is None:
            self.head = min
        else:
            prev_curr.next = min
        prev_min.next = curr
        temp = min.next
        min.next = curr.next
        curr.next = temp

    def selection_sort(self):
        curr = self.head
        prev_curr = None

        while curr is not None:
            prev_min = prev_curr
            min = curr
            prev = curr
            sub_curr = curr.next
            while sub_curr is not None:
                if sub_curr.value < min.value:
                    min = sub_curr
                    prev_min = prev
                prev = sub_curr
                sub_curr = sub_curr.next
            if min is not curr:
                self.swap(prev_curr, curr, prev_min, min)
                curr = min
            prev_curr = curr
            curr = curr.next
        return


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

