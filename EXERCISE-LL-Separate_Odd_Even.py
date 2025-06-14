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
            print(temp.value, end="->")
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

    def separate_odd_even_indexes(self):
        if self.head is None:
            return 
        prev = None
        even = self.head
        odd = even.next
        curr_odd_list = None
        odd_list = None

        while odd:
            # Create a odd_list
            if odd_list:
                curr_odd_list.next = odd
                curr_odd_list = curr_odd_list.next
            else:
                odd_list = odd
                curr_odd_list = odd
            
            # Preserve Tail
            ll.tail = curr_odd_list 
            
            # The actual detach part
            even.next = odd.next
            odd.next = None
            prev = even
            even = even.next
            odd = None if even is None else even.next
        
        # Finally attached two list..
        
        if even:
            # Case when length of the list is odd
            even.next = odd_list
        else:
            # Case when length of the list is even
            prev.next = odd_list
        return

ll = LinkedList(0)
#ll.append(1)
#ll.append(2)
#ll.append(3)
#ll.append(4)

print("\n\n")
print(f"Before Swapping:")
print(ll.print_list())
ll.separate_odd_even_indexes()
print(f"\n\nAfter Swapping:")
print(ll.print_list())
print("\n\n")