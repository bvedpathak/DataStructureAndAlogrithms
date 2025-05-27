def max_subarray(nums):
    if nums is None or len(nums) < 1:
        return 0
    result = list(range(len(nums)))
    max_sum = nums[0]
    result[0] = nums[0]
    for i in range(1,  len(nums)):
        if nums[i] > result[i-1] + nums[i]:
            result[i] = nums[i]
        else:
            result[i] = result[i-1] + nums[i]
        if max_sum < result[i]:
            max_sum = result[i]
    return max_sum


# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)

# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2)

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3)

"""
    EXPECTED OUTPUT:
    ----------------
    Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    Result: 6
    Example 2: Input: [1, 2, 3, -4, 5, 6] 
    Result: 13
    Example 3: Input: [-1, -2, -3, -4, -5] 
    Result: -1

"""