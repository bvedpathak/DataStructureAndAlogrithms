# A rotated sorted is an array of numbers sorted in ascending order, in which
# a potion of the array is moved from the begining to the end. 
# The funciton focuses on finding the target in such rotated array using Binary
# search.
def find_target_in_rotated_list(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        # If the left subarray [left : mid] is sorted, check if the
        # target falls in this range. If it does, search the left
        # subarray. Otherwise, search the right.
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right subbray [mid:right] is sorted, check if the
        # target falls in the range. If it does, search the right 
        # subarray. Otherwise, search the left.
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    # If the target is found in the array, return it's index. Otherwise,
    # return -1    
    return left if nums and nums[left] == target else -1

print("\n")
nums = [8, 9, 1, 2, 3, 4, 5, 6, 7]
target = 10
print(f"The target {target} in {nums} present at: {find_target_in_rotated_list(nums, target)}")

