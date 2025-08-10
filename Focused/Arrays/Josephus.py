# There are n people standing in a circle, numbered from 0 to n - 1. Starting from person 0,
# count k people clockwise and remove the kth person. After the removal, begin counting again
# from the next person still in the circle. Repeat this process until only one person remains, and
# return that person’s position.
# Time: O(n) Space: O(n) - due to stack used in recurrsion
def josephus(n, k):
    # Base case: If there's only one person, the last person is person 0
    if n == 1:
        return 0

    # Calculate the position of the last person remaining in the reduced 
    # problem with 'n - 1' people. We use module 'n' to ensure the answer
    # doesn't exceed the 'n - 1'
    return (josephus(n - 1, k) + k) % n

# Since the problem is recurrsive / subproblem in nature, it can be solved using
# dynamic programming as well where the DP formula would be:
# dp[i] = (dp[i - 1] + k) % i 
# since we are only refering a one past index here, we can optimize using one variable
# like below
# Time: O(n), Space: O(1) - We saved space compared to the recurrsive solution
def josephus_v1(n, k):
    res = 0
    for i in range(2, n + 1):
        # dp[i] = (dp[i - 1] + k) % i
        res = (res + k) % i

    return res

n = 5 
k = 2

print(f"\nLast Person standing in the queue of the length {n} would be: {josephus(n, k)}\n")
print(f"\nLast Person standing in the queue of the length {n} would be: {josephus_v1(n, k)}\n")