# Typical two-sum with O(n) approach
def two_sum_v1(nums, sum):
    lookup = dict()
    for num in nums:
        if sum - num in lookup:
            return [sum - num, num]
        lookup[num] = sum - num
    return None

# Brute Force approach - with O(n2)
def three_sum(nums, target):
    lookup = dict()
    for num in nums:
        result = two_sum_v1(nums, target - num) 
        if result is not None:
            result.append(num)
            return result
    return None

print("\n\n")
print(three_sum([1,2,3,5], 6))
print("\n\n")
     
        
        