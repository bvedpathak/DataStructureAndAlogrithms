import heapq

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

# Time: O(n.log k) = O(k.log k) to create initial heap + for n node push/pop taking O(log k)
def merge_k_sorted_lists(input_lists):
    if not input_lists:
        return None
    heap = []
    result_list = LinkedList(-1)
    # Define the custom comparator for the Node
    Node.__lt__ = lambda self,other: self.value < other.value

    # Push the head of the each list to the heap
    for lst in input_lists:
        if lst:
            heapq.heappush(heap,lst.head)
    # Create a pointer to the new list which we will adding new elements to (from the heap)
    curr = result_list.head
    while heap:
        # Pop the node from the heap having smallest value and add to the new list. 
        smallest_node = heapq.heappop(heap)
        curr.next = smallest_node
        curr = curr.next
        # The smallest node may have next node (which may / may not be smaller) so add it to the heap
        # help will take care of bubbling the smallest at the moment
        if smallest_node.next:
            heapq.heappush(heap, smallest_node.next)
    # We had created a dummy -1 head so lets take that out and return the new list
    result_list.head = result_list.head.next
    return result_list

l1 = LinkedList(1)
l1.append(6)

l2 = LinkedList(1)
l2.append(4)
l2.append(6)

l3 = LinkedList(3)
l2.append(7)
l2.append(8)

input_lists = [l1, l2, l3]

print("\n")
result = merge_k_sorted_lists(input_lists)
print(f"Result of the merged K sorted list is: {result.print_list() if result else None}")