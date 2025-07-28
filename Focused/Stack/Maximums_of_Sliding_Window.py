from collections import deque

# It is the same algo as maintaining a max on top of the stack/datastructure
# the main use of deque here vs stack is because it is 'sliding window' so we
# need to remove elements as well as window is slided thus we use deque
# Time: O(n) and Space: O(k)
def maximums_of_sliding_window(nums, k):
    res = []
    dq = deque()
    left = right = 0

    while right < len(nums):
        # 1) Ensure the values of the deque maintain a monotonic decreasing order
        # by removing candidates <= the current candidate
        
        while dq and dq[-1][0] < nums[right]:
            dq.pop()
        
        # 2) Add the current candidate

        dq.append((nums[right], right))

        # If the window is of length 'k', record the maximum of the window
        if right - left + 1 == k:
            # 3) Remove values whoes indexes occur outside the window
            if dq and dq[0][1] < left:
                dq.popleft()
            # Since we are already maintaining the max value at the leftmost side of the queue
            # append that to the result set for the current window
            res.append(dq[0][0])
            # Slide the window by advancing both 'left' and 'right'. Remember that right 
            # pointer always gets advanced so we just need to advance the 'left'
            left += 1
        right += 1
    return res

print("\n")

nums = [3, 2, 4, 1, 2, 1, 1]
k = 4

print(f"Maximums of Sliding window for the array {nums} are: {maximums_of_sliding_window(nums, k)}")

