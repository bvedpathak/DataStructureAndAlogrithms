# Brute force method with O(n2) time complexity and O(1) space complexity
def two_sum(nums, sum):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] == sum - nums[i]:
                return [nums[i], nums[j]]
    return None

# Optimal solution with O(n) time complexity and O(n) space complexity
def two_sum_v1(nums, sum):
    lookup = dict()
    for num in nums:
        if sum - num in lookup:
            return [sum - num, num]
        lookup[num] = sum - num
    return None

print("\n\n")
print(two_sum_v1([1,2,3,5], 1))
print("\n\n")
