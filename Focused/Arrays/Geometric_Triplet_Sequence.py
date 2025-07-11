# Time: O(n) and Space: O(n)
def how_many_geometric_triplet_sequences(nums, r):
    result = 0
    left_map = {}
    right_map = {}
    # As a start populate the right map first..as we progress the array, we will
    # populate the left map. For the first element, the left map will be empty
    for num in nums:
        right_map[num] = right_map.get(num,0) + 1

    for num in nums:
        # Reduce the frequency of the current number from right_map
        right_map[num] = right_map.get(num) - 1 if right_map.get(num) > 0 else 0 
        if num % r == 0:
            result += left_map.get(num//r, 0) * right_map.get(num*r, 0)
        # The current number/frequency will be part of left map so add that
        left_map[num] = left_map.get(num, 0) + 1
    
    return result

print("\n")
nums = [2, 1, 2, 4, 8, 8]
r = 2
print(f"Numf of geometric triplet in the list {nums} for {r} are: {how_many_geometric_triplet_sequences(nums, r)}")
print("\n")