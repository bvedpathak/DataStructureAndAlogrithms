## Standard recurrsive way to get the minimum coins needed to 
## form a denomination
## We can do tons of optimization here a) using memoization but that wont be that 
## effective for this usecase (already shown a function with memoization)
## or adding some checkes on if minimum number solution already exist then do not even try
## the solutions that are using more coins (especially when the goal is return minimum set)
def denomination(coins, n, curr, result):
    if coins is None or len(coins) < 1:
        return result
    if n == 0:
        if len(result) == 0:
            result.append(curr[:])
        elif len(curr) > 0 and len(result[0]) > len(curr):
            result[0] = curr[:]
        return result
    if n < 0:
        return result
    
    for i in range(len(coins)):
        ## more checks can be added here to give up if len(curr) is already larger
        ## then len(result[0])
        if coins[i] <= n:
            curr.append(coins[i])
            result = denomination(coins, n - coins[i], curr, result)
            curr.pop()
    
    return result

## Standard recurrsive way to get the minimum coins needed to 
## form a denomination
def denomination_with_memo(coins, n, curr, result, memo):
    if coins is None or len(coins) < 1:
        return result
    if n == 0:
        if len(result) == 0:
            result.append(curr[:])
        elif len(curr) > 0 and len(result[0]) > len(curr):
            result[0] = curr[:]
        return result
    
    if n in memo:
        return memo[n]
    
    if n < 0:
        return result
    
    for i in range(len(coins)):
        if coins[i] <= n:
            curr.append(coins[i])
            result = denomination(coins, n - coins[i], curr, result)
            memo[n] = result
            curr.pop()
    
    return result

## Another tryout for ALL Combinations:
def denomination_v1(coins, n, ans, curr, index):
    if not coins:
        return
    if n < 0:
        return
    if n == 0:
        ans.append(curr[:])
    
    for i in range(index, len(coins)):
        curr.append(coins[i])
        denomination_v1(coins, n - coins[i], ans, curr, index)
        curr.pop()
    return


## Same (not the actual combinations though but minimum combinations) using DP
def denomination_with_dp(coins, n):
    dp = [float('inf')] * (n+1)
    dp[0] = 0 ## Zero can be made with zero coins

    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[n] if dp[n] != float('inf') else -1

coins = [5, 10, 2]
n = 37
result = []
memo = {}
print("\n\n")
print(f"Standard Recurrsion: Possible combinations to achieve {n} are {denomination(coins, n, [], result)}")
result = []
print(f"Recurrsion with Memoization: Possible combinations to achieve {n} are {denomination_with_memo(coins, n, [], result, memo)}")

#ans = []
#print(f"Standard Recurrsion: ALL combinations to achieve {n} are {denomination_v1(coins, n, ans, [], 0)} {ans}" )

print(f"Using DP: Min coins needed to achieve {n} are {denomination_with_dp(coins, n)}")
print("\n\n")
