class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse(self):
        if self is None or self.head is None:
            return
        curr = self.head
        before = None
        while curr is not None:
            after = curr.next
            curr.next = before
            curr.prev = None
            if before is not None:
                before.prev = curr
            before = curr
            curr = after
        temp = self.head
        self.head = self.tail
        self.tail = temp
        return

    def reverse(self, start, len):
        if len <= 1:
            return start
        before = start.prev
        after = None
        temp = start
        for _ in range(len):
            after = temp.next
            temp.next = before
            ##temp.prev = None
            if before is not None:
                before.prev = temp
            before = temp
            if after is None:
                break
            temp = after
        start.next = after
        return before

    def reverse_between(self, start, end):
        if self is None or self.head is None:
            return
        #prev = None
        curr = self.head
        count = 0
        while curr is not None:
            if count == start:
                if curr.prev is None:
                    self.head = self.reverse(curr, end - start + 1)
                else:
                    curr.prev.next = self.reverse(curr, end - start + 1)
                return
            count += 1
         #   prev = curr
            curr = curr.next
        return


# Test Cases
print("\nTest 1: Middle segment reversal")
dll1 = DoublyLinkedList(3)
for v in [8, 5, 10, 2, 1]:
    dll1.append(v)
print("BEFORE: ", end="")
dll1.print_list()
dll1.reverse_between(1, 4)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest 2: Full list reversal")
dll2 = DoublyLinkedList(1)
for v in [2, 3, 4, 5]:
    dll2.append(v)
print("BEFORE: ", end="")
dll2.print_list()
dll2.reverse_between(0, 4)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest 3: No-op on single node")
dll3 = DoublyLinkedList(9)
print("BEFORE: ", end="")
dll3.print_list()
dll3.reverse_between(0, 0)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest 4: Reversal with head involved")
dll4 = DoublyLinkedList(7)
for v in [8, 9]:
    dll4.append(v)
print("BEFORE: ", end="")
dll4.print_list()
dll4.reverse_between(0, 2)
print("AFTER:  ", end="")
dll4.print_list()

