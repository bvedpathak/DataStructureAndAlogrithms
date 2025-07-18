import heapq
# Kth largest number can be implemented many ways e.g. Stardard Sort, Min Heap or using QuickSort
# The standard sort sorts all n elements whereas we only need k elements to be sorted: Time: O(n.log n)
# Min-Heap is optimized one where we only maintain k sorted so Time: O(n. log k). 
# The quickSort way is the most efficient but will write that in another section. This section is for heap way

# Standard sort way
# Time: O(n log n), Space: O(1)

def kth_largest_using_sort(nums, k):
    if not nums or k >= len(nums):
        return None
    nums = sorted(nums)
    return nums[len(nums) - k]


def kth_largest_using_min_heap(nums, k):
    if not nums or k >= len(nums):
        return None
    
    min_heap = []
    heapq.heapify(min_heap)

    for num in nums:
        # Ensure the heap as at least 'k' integers
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        # If num is greater than the smallest integet in the heap, pop off this smallest
        # integet from the help and push in num
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return min_heap[0]

k = 3
nums = [6, 8, 4, 2, 7, 3, 1, 5]

print("\n")
print(f"kth largest using Standard Sort: {kth_largest_using_sort(nums, k)}")
print(f"kth largest using Min Heap: {kth_largest_using_sort(nums, k)}")

