# Given an array of 0s, 1s, and 2s representing red, white, and blue, respectively, sort the array in
# place so it resembles the Dutch national flag, with all reds (0s) coming first, followed by whites
# (1s), and finally blues (2s).
# Example:
# Input: nums = [0, 1, 2, 0, 1, 2, 0]
# Output: [0, 0, 0, 1, 1, 2, 2]
# Basically it is a sorting problem just that since we have only 3 types of values
# we can do better than the standard O(n. log n) using the contraints. In short, it 
# is a two pointer technique
# Time: O(n), Space: O(1)
def duch_national_flag(nums):
    if not nums:
        return False
    l = i = 0
    r = len(nums) - 1
    while i <= r:
        # Swap 2s with the element at the right pointer
        if nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        # Swap 0s with the element at the left pointer
        elif nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
            i += 1
        else:
            i += 1
    # Return the in-place sorted array
    return nums

nums = [0, 1, 2, 0, 1, 2, 0]
#nums = [2, 2, 2, 2, 2, 2, 2]


print(f"\nDutch National Flag sorting of {nums} will be: {duch_national_flag(nums)}\n")