## Intiution / Basic method of sorting the array first and then finding the longest sequece
## Time: O(n.log n) Space: O(1)
def longest_consecutive_sequence(nums):
    if nums is None:
        return None
    if len(nums) < 1:
        return 0
    
    nums = sorted(nums)
    max_sequence = 0
    count = 1
    for i in range(1, len(nums)):

        if nums[i] - nums[i-1] == 1:
            count += 1
            max_sequence = max(max_sequence, count)
        else:
            count = 1

    return max_sequence

## Optimal approach by using an extra space. First we add elements into the hash set
## then while iterating thru the nums, we see if the curr num is the min of the chain/sequence
## by chekcing if num - 1 exists in the set, if curr num is min, we calculate the chain length and
## store the max
## Time: O(n), Space: O(n)
def longest_consecutive_sequence_v1(nums):
    if nums is None:
        return None
    if len(nums) < 1:
        return 0
    
    lookup = set(nums)

    max_chain_count = 0

    for num in nums:
        if num - 1 not in lookup:
            curr_num = num
            curr_chain = 1
        while (curr_num + 1) in lookup:
            curr_num += 1
            curr_chain += 1
        
        max_chain_count = max(max_chain_count, curr_chain)

    return max_chain_count
        
nums = [1, 6, 2, 5, 8, 7, 10, 3]
print("\n")
print(f"Longest Sub-sequence in {nums} is: {longest_consecutive_sequence(nums)}")
print(f"Longest Sub-sequence in {nums} is: {longest_consecutive_sequence_v1(nums)}")
print("\n")