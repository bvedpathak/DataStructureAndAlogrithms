# Implementation of queue using stack
# Time: O(n) for dequeue / peek and O(1) for enqueue
class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, x):
        self.enqueue_stack.append(x)

    def transfer_enqueue_to_dequeue(self):
        # If the dequeue stack is empty, push all elements from the enqueue stack onto
        # the dequeue stack. This ensures the top of the dequeue stack contains the 
        # least recently added value
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

    def dequeue(self):
        self.transfer_enqueue_to_dequeue()
        # Pop and return the value at the top of the dequeue stack. 
        return self.dequeue_stack.pop() if self.dequeue_stack else None
    
    def peek(self):
        self.transfer_enqueue_to_dequeue()
        return self.dequeue_stack[-1] if self.dequeue_stack else None
    
print("\n")
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(f"Dequeued: {q.dequeue()}")
print(f"Dequeued: {q.dequeue()}")
print(f"Peek: {q.peek()}")
