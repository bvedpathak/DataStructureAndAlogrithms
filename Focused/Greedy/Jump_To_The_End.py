# Check to see if we can reach the end of the array from index 0
def jump_to_the_end(nums):
    if not nums:
        return False
    
    # Set the initial destination to the last index of the array
    destination = len(nums) - 1

    # Traverse the array in the reverse to see if the destination can be
    # reached by earlier indexes
    for i in range(len(nums) - 1, -1, -1):
        # If we can reach the destination from the current index,
        # set this index as the new destination
        if i + nums[i] >= destination:
            destination = i
    # If the destination index 0, we can jump to the end from the index 0
    return destination == 0

print("\n")
nums = [9, 6, 7, 0, 4, 2, 0, 5]
print(f"Which is the earliest index from {nums} allows to reach to the destination: {jump_to_the_end(nums)}")