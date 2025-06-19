def max_profit(nums):
    end = 0
    start = end
    max_profit = 0
    while end < len(nums):
        if nums[end] - nums[start] > 0:
            max_profit = max(max_profit, nums[end] - nums[start])
        else:
            start = end
        end += 1
    return max_profit

def max_profit_dp(nums):
    profit = 0
    buy_price = float("Inf")
    profit = 0

    for i, price in enumerate(nums):
        if price < buy_price:
            buy_price = price
        else:
            profit = max(price - buy_price, profit)

    return profit

nums = [5, 3, 7, 8, 2, 3, 4]
print("\n\n")
print(f"Max Profit with normal algorithm: {max_profit(nums)}")
print(f"Max Profit with normal algorithm: {max_profit_dp(nums)}")
print("\n\n")