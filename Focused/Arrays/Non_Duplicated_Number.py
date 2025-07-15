import math
# Solution with O(n) time complexity and O(n) space complexity
def find_single_number(nums):
    lookup = dict()
    for num in nums:
        if num in lookup:
            lookup[num] = False
        else:
            lookup[num] = True
    
    for k, v in lookup.items():
        if v == True:
            return k
    return None

# Similar solution with sum method 2*Sum(unique nums) - actual sum
def find_single_number_v1(nums):
    unique = set()
    ideal_sum = 0
    actual_sum = 0
    for num in nums:
        if num not in unique:
            ideal_sum += 2*num
            unique.add(num)
        actual_sum += num
    return ideal_sum - actual_sum

# The best solution with O(n) time complexity but O(1) space complexity
# with XOR magic
def find_single_number_v2(nums):
    if not nums:
        return None
    
    result = nums[0]
    for i in range(1, len(nums)):
        result ^= nums[i]
    return result

print("\n\n")
print(f"Single Number in the given list is: {find_single_number_v2([1,2,1,2,3,11,11,4,4,5,5,7,7])}")
print("\n\n")
