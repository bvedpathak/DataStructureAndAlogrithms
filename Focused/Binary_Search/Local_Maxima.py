# A local maxima is a value greater than both its left and right immediate neighbors
# imagine it is a kind of peak comapre to its left and right neighbors
# There can be many local maximas in the given array
def local_maxima(nums):
    if not nums:
        return -1
    
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1

    return nums[l]

#nums = [1, 4, 3, 2, 3]
nums = [0, 4, 3, 1, 0]
print(f"Local maxima for {nums} is: {local_maxima(nums)}")