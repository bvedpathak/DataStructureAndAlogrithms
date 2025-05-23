## Below function solves the problem but with O(n2)
'''
def subarray_sum(nums, target):
    for i in range(len(nums)):
        sum = nums[i]
        if sum == target:
            return [i, i]
        for j in range(i + 1, len(nums)):
            sum += nums[j]
            if sum == target:
                return [i, j]
    return []
'''

def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        diff = current_sum - target
        if diff in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
