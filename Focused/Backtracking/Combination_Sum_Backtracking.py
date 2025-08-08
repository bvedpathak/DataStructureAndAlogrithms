# Given an integer array and a target value, find all unique combinations in the array where the
# numbers in each combination sum to the target. Each number in the array may be used an
# unlimited number of times in the combination.
# Example:
# Input: nums = [1, 2, 3], target = 4
# Output: [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]
# Constraints:
# All integers in nums are positive and unique.
# The target value is positive.
# The output must not contain duplicate combinations.

def combination_sum(nums, target, ans, curr, curr_sum, index):
    if not nums:
        return 
    
    if curr_sum == target:
        ans.append(curr[:])
    elif curr_sum < target: 
        for i in range(index, len(nums)):
            curr.append(nums[i])
            combination_sum(nums, target, ans, curr, curr_sum + nums[i], i)
            curr.pop()
    return

ans = []
nums = [2,3,6]
target = 8

print("\n\n")
combination_sum(nums, target, ans, [], 0, 0)
print(f"Combinations adding up to the {target} are: {ans}")
print("\n\n")

'''
            
                2                       3                       6
            2       
        2   3   6
    2   3(x)    6(x)
        6(x)

'''