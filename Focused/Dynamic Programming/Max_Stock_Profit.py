# Two pointer techique to solve the same problem
def max_profit(nums):
    start = end = 0
    max_profit = 0
    while end < len(nums):
        if nums[end] - nums[start] > 0:
            max_profit = max(max_profit, nums[end] - nums[start])
        else:
            start = end
        end += 1
    return max_profit

# DP technique with defining DP array so 
# Time: O(n), Space: O(n)
def max_profit_dp(nums):
    if not nums:
        return None
    max_profit = 0

    dp = [0 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i], nums[i] - nums[i-1] + dp[i-1])
        max_profit = max(max_profit, dp[i])
    
    return max_profit

# Running total DP technique w/o explicitly defining dp array
def max_profit_dp_v1(nums):
    profit = 0
    buy_price = float("Inf")

    for price in nums:
        if price < buy_price:
            buy_price = price
        else:
            profit = max(price - buy_price, profit)

    return profit

nums = [5, 3, 7, 8, 2, 3, 4]
print("\n\n")
print(f"Max Profit with normal algorithm: {max_profit(nums)}")
print(f"Max Profit with dp algorithm: {max_profit_dp(nums)}")
print(f"Max Profit with dp algorithm: {max_profit_dp_v1(nums)}")
print("\n\n")