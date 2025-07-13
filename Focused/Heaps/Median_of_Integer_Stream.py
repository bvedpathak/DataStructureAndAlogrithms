import heapq
# Time: O(log(n)) for add()
# Time: O(1) for get_median()
class MedianOfAnIntegerStream:
    def __init__(self):
        self.left_half = [] # Max-heap
        self.right_half = [] # Min-heap

    def add(self, num):
        # If num is less than or equal to the max of left_half i.e. max_heap, it belongs
        # to the left half
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)

            # rebalance the heaps to maintain close to equal elements in them
            if len(self.left_half) > len(self.right_half):
                heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        # Otherwise belongs to the right half
        else:
            heapq.heappush(self.right_half, num)

            # rebalance the heaps to maintain close to equal elements in them
            if len(self.right_half) > len(self.left_half):
                heapq.heappush(self.left_half, -heapq.heappop(self.right_half))
    
    def get_median(self):
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2.0
        return -self.left_half[0]

print("\n")
action = MedianOfAnIntegerStream()
action.add(0)
action.add(1)
action.add(2)
action.add(3)
print(action.get_median())
action.add(4)
action.add(5)
action.add(6)
action.add(7)
print(action.get_median())