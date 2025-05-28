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

def max_water_container(nums):
    if nums is None or len(nums) < 1:
        return [0, 0, 0]
    max_area = 0
    start_index = 0
    end_index = 0
    tall_so_far = nums[0]
    tall_index = 0

    for i in range(1, len(nums)):
        y = tall_so_far if tall_so_far < nums[i] else nums[i]
        x = i - tall_index
        area = x * y

        if area > max_area:
            max_area = area
            start_index = tall_index
            end_index = i

        if tall_so_far <= nums[i]:
            tall_so_far = nums[i]
            tall_index = i
    return [start_index, end_index, max_area]

print(f"\nStart Index, End Index and Area is: {max_water_container([5,9,2,1,4])}")

## Amother solution for the above container problem:

def maxArea(height):
    maxarea = 0
    l = 0
    r = len(height)-1

    while(l<r):
        maxarea = max(maxarea, min(height[l],height[r])*(r-l))
        if(height[l]<height[r]):
            l+=1
        else:
            r-=1
    return maxarea


# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("\n\nExample 1: Input:", input_case_1, "\nResult:", result_1)

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