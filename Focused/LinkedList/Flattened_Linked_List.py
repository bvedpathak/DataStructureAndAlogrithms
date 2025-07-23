class MultiLevelListNode:
    def __init__(self, val, next, child):
        self.val = val
        self.next = next
        self.child = child

    def print_list(self, head):
        values = []
        temp = head
        while temp is not None:
            values.append(str(temp.val))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

def flatten_multi_level_list(head):
    if not head:
        return None
    
    tail = head

    while tail.next:
        tail = tail.next
    
    curr = head

    while curr:
        if curr.child:
            tail.next = curr.child
            curr.child = None
            while tail.next:
                tail = tail.next
        curr = curr.next
    return head

lst = MultiLevelListNode(1, None, None)
lst.next = MultiLevelListNode(2, None, MultiLevelListNode(6, None, None))
lst.next.next = MultiLevelListNode(3, None, None)
lst.next.next.next = MultiLevelListNode(4, None, None)

lst.print_list(lst)
flatten_multi_level_list(lst).print_list(lst)