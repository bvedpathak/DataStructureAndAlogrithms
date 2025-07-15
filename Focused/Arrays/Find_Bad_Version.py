# The method picks the first bad version (arbitrary)
def isBadVersion(n):
    if n >= 2:
        return True
    return False

## Brute Force method with O(n) time complexity
def find_first_bad_version(nums):
    for num in nums:
        if isBadVersion(num):
            return num 
    return None

## An Optimal solution with divide and conquer (Binary Search)
## Time: O(log n)
def find_first_bad_version_v1(nums):
    if not nums:
        return None
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if isBadVersion(nums[mid]):
            r = mid
        else:
            l = mid + 1
    return nums[l]

print("\n\n")
print(find_first_bad_version_v1([1,2,3,4,5,6,7,8,9,10]))
print("\n\n")