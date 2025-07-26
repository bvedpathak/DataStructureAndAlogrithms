## Dynamic Programming way of solving
def which_zero_to_flip_with_dp(nums):
    if nums is None or len(nums) < 1:
        return -1
    
    lookup = [0] * len(nums)
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        
        lookup[i] = count

    result = -1
    max_so_far = 0
    for i in range(1, len(lookup)):

        if nums[i] != 1:
            sum = lookup[i-1] + lookup[i+1] if i < len(lookup) - 1 else 0

            if max_so_far < sum:
                max_so_far = sum
                result = i
    
    return result if max_so_far > 0 else -1 

def which_zero_to_flip_with_sliding_window(nums):
    if nums is None or len(nums) < 1:
        return -1
    
    start = 0
    max_so_far = 0
    result = -1
    count = 0
    first_zero_passed = False

    while start < len(nums):
        count += 1

        if nums[start] != 1:
            if count > max_so_far:
                max_so_far = count
                result = start
            if not first_zero_passed:
                first_zero_passed = True
            else:
                count = 0
        start += 1 
    return result if max_so_far > 2 else -1


print("\nResults with DP:")
print(f"The position at which a zero needs to be flipped is: {which_zero_to_flip_with_dp([1,1,0,1,1,1,1,0,1,1,1,1,0,1])}")
print(f"The position at which a zero needs to be flipped is: {which_zero_to_flip_with_dp([0,0,0,1,1,1,1,0,1,1,1,1,0,1])}")
print(f"The position at which a zero needs to be flipped is: {which_zero_to_flip_with_dp([0,0,0,0,0,0,0,0,0,0,0,0,0,0])}")
print(f"The position at which a zero needs to be flipped is: {which_zero_to_flip_with_dp([1,1,1,1,1,1,1,1,1,1,1,1,1,1])}")

print("\nResults with Sliding Window:")
print(f"The position at which a zero needs to be flipped is: {which_zero_to_flip_with_sliding_window([1,1,0,1,1,1,1,0,1,1,1,1,0,1])}")
print(f"The position at which a zero needs to be flipped is: {which_zero_to_flip_with_sliding_window([0,0,0,1,1,1,1,0,1,1,1,1,0,1])}")
print(f"The position at which a zero needs to be flipped is: {which_zero_to_flip_with_sliding_window([0,0,0,0,0,0,0,0,0,0,0,0,0,0])}")
print(f"The position at which a zero needs to be flipped is: {which_zero_to_flip_with_sliding_window([1,1,1,1,1,1,1,1,1,1,1,1,1,1])}")
print("\n")