## Brute Force Solution without using any formula
## Time: O(n Log n), Space: O(1)
def find_missing_number_in_sequence(nums):
    sorted_nums = sorted(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] - sorted_nums[i - 1] > 1:
            return sorted_nums[i - 1] + 1
    return -1

## Optimal Solution using a math formula
def find_missing_number_in_sequence_v1(nums):
    n = len(nums)
    # May not be needed but just in case if the sequence 
    # does not start with 0
    start = min(nums)
    if start > 0:
        n = n + start
        start = start - 1
    missing_sum = start * (start + 1)//2
    
    ideal_sum = (n * (n+1)//2) 
    actual_sum = missing_sum
    for num in nums:
        actual_sum += num
    return ideal_sum - actual_sum

print(f"Missing Number from the sequence is: {find_missing_number_in_sequence_v1(([3,5,6,7,8]))}")