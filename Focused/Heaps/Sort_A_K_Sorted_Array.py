import heapq
# A partial array is sorted post given k elements. So first k elements are not sorted
# as we know, we can use any sorted algorithm here with n.log n complexity but since 
# partial array is sorted post K, we can improvise to do n. log k with heap
def sort_a_k_sorted_array(nums, k):
    if not nums:
        return None
    
    # Populate a min-heap with the first k + 1 values in 'nums'
    min_heap = nums[:k+1]
    heapq.heapify(min_heap)

    # Replace the elements in the array with the minimum from the heap at each iteration
    insert_index = 0
    for i in range(k+1, len(nums)):
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
        heapq.heappush(min_heap, nums[i])

    # Pop the remaining elements from the heap to finish sorting the array
    while min_heap:
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
    
    return nums

nums = [5, 1, 9, 4, 7, 10]
k = 2

print("\n")
print(f"Sorted Array {sort_a_k_sorted_array(nums, k)}")