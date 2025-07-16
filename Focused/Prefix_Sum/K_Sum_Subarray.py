# Time: O(n2) and Space: O(n)
def k_sum_subarrays_v1(nums, k):
    n = len(nums)
    count = 0

    prefix_sum = [0]

    # Pre calculate the pre-fix sum
    for i in range(0,n):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    # Loop thru all valid pairs of prefix sum values to find all
    # subarrays that sum to 'k'

    for j in range(1, n + 1):
        for i in range(1, j + 1):
            if prefix_sum[j] - prefix_sum[i - 1] == k:
                count += 1
    return count

# Time: O(n), Space: O(n)
def k_sum_subarrays_v2(nums, k):
    if not nums:
        return None
    count = 0
    # Initiatiaze the map with 0 to handle subarrays that sum to 'k'
    # from the start of the array
    prefix_sum_map = {0 : 1}
    curr_prefix_sum = 0

    for num in nums:
        # Update the running prefix sum by adding the current number.
        curr_prefix_sum += num

        # If a subarray with a sum 'k' exists, increment 'count' by the number of times
        # it has been found so far.
        if curr_prefix_sum - k in prefix_sum_map:
            count += prefix_sum_map.get(curr_prefix_sum - k) 
        
        # Update the ferquency of 'curr_prefix_sum' in the hash map
        prefix_sum_map[curr_prefix_sum] = prefix_sum_map.get(curr_prefix_sum, 0) + 1

    return count

print("\n")
nums = [1, 2, -1, 1, 2]
k = 3

print(f" {3} can be obtain by adding total {k_sum_subarrays_v1(nums, k)} subarrays")


