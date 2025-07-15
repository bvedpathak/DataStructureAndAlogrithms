## My Version (before looking at the solution)
def is_mountain(nums):
    if nums is None or len(nums) < 3:
        return False
    up = True
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            if up is False:
                return False
        elif nums[i-1] > nums[i]:
            if i - 1 == 0:
                return False
            if up is True:
                up = False
        else:
            return False
    return up == False

## Solution from the course
def validMountainArray(A):
    if len(A) < 3:
        return False
    i = 1
    while (i < len(A) and A[i] > A[i - 1]):
        i += 1

    # We stayed where we were OR we reached at the end continously climbing
    # that means it is not the mountain array
    if (i == 1 or i == len(A)):
        return False

    # Now keep going down as much as possible
    while (i < len(A) and A[i] < A[i - 1]):
        i += 1
    # If we reach to the end of the list, if we reach at the
    # end of the array means, we reach the downhill without 
    # encountering any uphill..which means a valid mountain array
    return i == len(A)

print(f"is Mountain: {is_mountain([1,2,3,4,3,2,1])}")