def isBadVersion(n):
    if n >= 1:
        return True
    return False

## Brute Force method with O(n) time complexity
def find_first_bad_version(nums):
    for num in nums:
        if isBadVersion(num):
            return num 
    return None

## An Optimal solution with divide and conquer
def find_first_bad_version_v1(nums):
    if nums is None or len(nums) < 1:
        return None
    start = 0
    end = len(nums) 
    mid = (start + end) // 2
    while mid >= start and mid < end:
        if isBadVersion(nums[mid]):
            end = mid 
        else:
            start = mid
        mid = (start + end) // 2
        if mid == len(nums) - 1:
            break
    return end if end < len(nums) else -1

print("\n\n")
print(find_first_bad_version_v1([1,2,3,4,5,6,7,8,9,10]))
print("\n\n")