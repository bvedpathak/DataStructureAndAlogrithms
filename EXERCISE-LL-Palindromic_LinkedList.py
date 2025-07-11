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

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def reverse_recursively(self, node):
        if (not node) or (not node.next):
            return node
        new_node = self.reverse_recursively(node.next)
        node.next.next = node
        node.next = None
        return new_node
    
    def reverse_from(self, node):
        prev, curr = None, node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def palindromic_linkedlist(self):
        
        mid = self.find_middle()

        second_head = self.reverse_from(mid)

        ptr1, ptr2 = self.head, second_head
        result = True
        while ptr2:
            if ptr1.value != ptr2.value:
                result = False
            ptr1, ptr2 = ptr1.next, ptr2.next
        return result
    
    def find_middle(self):
        fast = slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(1)
#my_linked_list.append(4)

print('Current LL:')
my_linked_list.print_list()
print(f"Is palindromic linkedlist? {my_linked_list.palindromic_linkedlist()}")
