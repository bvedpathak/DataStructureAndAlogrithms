# [1, 2, 2, 2, 3] element's positions to be found are 2. 
# Answer: [1, 3] as first position of 2 is 1 and last one is 3. 
# More info: The input array is sorted 

# Brute force method 
def find_positions(nums, target):
    if len(nums) < 1:
        return [-1,-1]
    left = 0
    right = len(nums) - 1
    left_index_found = -1
    right_index_found = -1
    while left < right:
        if left_index_found == -1 and nums[left] == target :
            left_index_found = left
        if right_index_found == -1 and nums[right] == target:
            right_index_found = right
        if left_index_found != -1 and right_index_found != -1:
            return [left_index_found, right_index_found]
        left += 1
        right -= 1
    # Solving for the case where there is only one element
    if left_index_found * right_index_found != 1:
        max_value = max(left_index_found, right_index_found)
        left_index_found = right_index_found = max_value
    return [left_index_found, right_index_found]


## This one is the optimized version where we are doing binary search
# to narrow down the search area instead of traversing thru the whole
# array
def find_positions_v1(nums, target):
    start = binary_search_index(nums,target)
    if start == -1:
        return [-1, -1]
    left = start
    right = start

    while left >= 0 and nums[left] == target:
        left -= 1
    
    while right < len(nums) and nums[right] == target:
        right += 1
    return [left + 1, right - 1]


# Typical recurssive binary search algorithm
def binary_search(nums, target):
    if nums is None or len(nums) < 0:
        return False
    if len(nums) == 1:
        return True if nums[0] == target else False
    mid = int(len(nums)/2)
    if nums[mid] == target:
        return True
    if nums[mid] < target:
        return(binary_search(nums[mid:], target))
    else:
        return(binary_search(nums[:mid+1], target))


# Iterative Binary Search algo which returns an index instead of 
# true or false
def binary_search_index(nums, target):
    if nums is None or len(nums) < 0:
        return -1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    start = 0
    end = len(nums)
    while start != end:
        mid =  (start + (end-start)//2)
        if nums[mid] == target:
            return mid
        if mid == len(nums) - 1 or mid <= 0:
            return -1 
        if nums[mid] < target:
            start = mid
            end = len(nums)
        else:
            start = 0
            end = mid
    return -1

print("\n\n")
print(find_positions_v1([10,11,11,11,17,18], 18))
print("\n\n")
#print(binary_search_index([1,2,4,5,6,7,8,9], 4))
print("\n\n")
