# Move Zeros to the End of an Array by copilot
def move_zeros(nums):
    """
    Move all zeros in the list to the end while maintaining the order of non-zero elements.
    
    :param nums: List of integers
    :return: List with all zeros moved to the end
    """
    zero_count = nums.count(0)
    nums[:] = [num for num in nums if num != 0] + [0] * zero_count
    return nums

# With using in-buit list methods like pop and append
def move_zeros_v1(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    return nums

# Bare metal i.e. without using any list methods
def move_zeros_v2(nums):
    i = 0 
    j = 0
    while i < len(nums):
        if nums[i] == 0:
            i += 1
        if i >= len(nums):
            return nums
        if i != j:
            nums[j] = nums[i]
            nums[i] = 0
        i += 1
        j += 1
    return nums

# Another approach
def moveZeroes_v3(nums):
    j = 0
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1
    for x in range(j, len(nums)):
        nums[x] = 0

print("\n\n")
print(move_zeros_v2([1,2,4,0,5,0,6,0]))
print(move_zeros_v2([0,0,4,0,5,0,6,0]))
print(move_zeros_v2([0,0,0,0,0,0,0,0]))
print(move_zeros_v2([0,0,0,0,0,0,0,1]))
print(move_zeros_v2([1,2,3,4,5,6,7,8]))

print("\n\n")

