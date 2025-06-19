## Standard recurrsive function without memoization 
def steps(curr, n):
    if curr == n:
        return 1
    if curr > n:
        return 0
    return (steps(curr + 1, n) + steps(curr + 2, n))

## Recurrsive function without memoization 
def steps_with_memoization(curr, n, lookup):
    if curr == n:
        return 1
    if curr > n:
        return 0
    
    if lookup[curr]:
        return lookup[curr]
    
    one_step = steps_with_memoization(curr + 1, n, lookup)
    lookup[curr + 1] = one_step
    two_steps = steps_with_memoization(curr + 2, n, lookup)
    lookup[curr + 2] = two_steps
    
    return (one_step + two_steps)

## Solution with Dynamic Programming (DP)
def steps_with_dp(n):
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

n = 4
lookup = [None] * (n+2)
print("\n\n")
print(f"Number of ways you can climb the steps {n} are: {steps(0, n)}")
print(f"Number of ways you can climb the steps with memoization {n} are: {steps_with_memoization(0, n, lookup)}")
print(f"Number of ways you can climb the steps with DP {n} are: {steps_with_dp(n)}")

print("\n\n")

