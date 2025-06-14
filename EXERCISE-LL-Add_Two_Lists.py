class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
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
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        i = 0
        temp_head = self.head
        while temp_head:
            if index == i:
                return temp_head
            i += 1
            temp_head = temp_head.next

        return temp_head


def add_two_lists(lst1 : LinkedList, lst2 : LinkedList, base : int):
    result = LinkedList()
    if lst1 is None:
        return lst2
    curr_lst1 = lst1.head
    curr_lst2 = lst2.head
    carryover = 0
    
    while curr_lst1 and curr_lst2:
        val = (curr_lst1.value + curr_lst2.value + carryover) % base
        carryover = (curr_lst1.value + curr_lst2.value + carryover) // base
        result.append(val)
        curr_lst1 = curr_lst1.next
        curr_lst2 = curr_lst2.next
    
    remainder_list = curr_lst1 if curr_lst1 is not None else curr_lst2
    
    while remainder_list:
        val = (remainder_list.value + carryover) % base  
        carryover = (remainder_list.value + carryover) // base
        result.append(val)
        remainder_list = remainder_list.next
    
    if carryover != 0:
        result.append(carryover)

    return result

lst1 = LinkedList()
lst1.append(1)
#lst1.append(1)
#lst1.append(1)

lst2 = LinkedList()
lst2.append(1)
lst2.append(1)
lst2.append(0)

print("\n\n")
print(lst1.print_list())
print(lst2.print_list())
print(add_two_lists(lst1, lst2, 10).print_list())
print("\n\n")

