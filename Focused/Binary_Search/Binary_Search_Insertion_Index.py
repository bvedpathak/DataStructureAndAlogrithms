# Find the given target using Binary Search and if the number
# is not present, return the index where it should be added
# Time: O(log n), Space: O(1)
def insertion_point_v1(nums, target):
    if nums is None or len(nums) < 1:
        return None
    left = 0
    right = len(nums) - 1

    while right - left > 1:
        mid = left + ((right - left) // 2)

        if nums[mid] == target:
            return mid
        
        if target > nums[mid]:
            left = mid
        else:
            right = mid
    
    if target < nums[left]:
        return left - 1 if left > 0 else left
    if target > nums[right]:
        return right + 1
    else:
        return right

# More clearner way of writing the same code above (No impact to time or space complexities)
def insertion_point_v2(nums, target):
    left , right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= target: ## Target is at the mid or somewhere left
            right = mid
        else:  ## Target is somewhere right
            left = mid + 1
    return left

print("\n")
nums = [1,2,4,5,7,8,9]
target = 6
print(f"Binary search insertion point for {target} in the {nums} is: {insertion_point_v1(nums, target)}")
print(f"Binary search insertion point for {target} in the {nums} is: {insertion_point_v2(nums, target)}")
print("\n")