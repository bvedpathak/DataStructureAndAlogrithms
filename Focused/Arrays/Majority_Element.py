# O(n) time complexity and O(n) space complexity
def majority_element(nums):
    lookup = dict()
    max_count = 0
    max_num = 0
    for num in nums:
        if num in lookup:
            lookup[num] = lookup.get(num) + 1
        else:
            lookup[num] = 0
        
        if max_count <= lookup.get(num):
            max_count = lookup.get(num)
            if max_count >= len(nums)//2:
                return num    
    return None

# Optimal solution using Boyer -- Moore majority vote algorithm
# The main constraint for the algo is that there is atleast one of the
# element of n/2 occrances exists. This solves using O(n) time and O(1) space
# complexity
def majority_element_v1(nums):
    count = 1
    candidate = nums[0]
    for i in range(1, len(nums)):
        current = nums[i]
        if candidate == current:
            count += 1
        else:
            count -= 1 
            if count == 0:
                candidate = current
                count = 1
    return candidate

print("\n\n")
print(f"Majority Element is: {majority_element_v1([4,1,4,2,4,4,5,4,6])}")
print("\n\n")
