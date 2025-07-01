# Brute force method with O(n2) time complexity and O(1) space complexity
def two_sum(nums, sum):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] == sum - nums[i]:
                return [nums[i], nums[j]]
    return None

# Another method of two_sum if we have a sorted array or we can
# sort the array 
# Time: O(n.log n), Space: O(1)
def two_sum_v1(nums, sum):
    if nums is None:
        return None
    nums = sorted(nums) 
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == sum:
            return [nums[i], nums[j]] 
        
        if nums[i] + nums[j] < sum:
            i += 1
        else:
            j -= 1
    return None
        

# Optimal solution with O(n) time complexity and O(n) space complexity
def two_sum_v2(nums, sum):
    lookup = dict()
    for num in nums:
        if sum - num in lookup:
            return [sum - num, num]
        lookup[num] = sum - num
    return None


print("\n\n")
print(two_sum_v1([5,1,3,2,5], 5))
print(two_sum_v2([5,1,3,2,5], 5))
print("\n\n")
