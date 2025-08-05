# You are a thief planning to rob a store. However, you can only carry a knapsack with a
# maximum capacity of cap units. Each item (i) in the store has a weight (weights[i]) and
# a value (values[i])
# Find the maximum total value of items you can carry in your knapsack
# Time: O(n * cap) Space: O((n + 1) * (cap + 1)
def knapsack(cap, weights, values):
    n = len(values)

    # Base case: Set the first column and last row to 0 by
    # initiazing the entire DP table to 0.

    dp = [[0 for _ in range(cap + 1)] for _ in range (n + 1)]

    # Populate the DP table
    for i in range(n - 1, -1, -1):
        for c in range (1, cap + 1):
            # If the item 'i' fits in the current knapsack capacity,
            # the maximum value at d[i][c] is the largest of either:
            # 1. The max value if we include item 'i'
            # 2. The max value if we exclude item 'i'.
            if weights[i] <= c:
                dp[i][c] = max(values[i] + dp[i + 1][c - weights[i]], dp[i + 1][c])
            # If it doesn't fit, we have to exclude it
            else:
                dp[i][c] = dp[i + 1][c]

    return dp[0][cap]

# As usual, we can optimize the DP 2D array to just using the latest and prev rows
# because we only need to lookback one historical row

def knapsack_optimized(cap, weights, values):
    n = len(values)
    # Initialize prev_row as the DP values of the row below the current row
    prev_row = [0 for _ in range(cap + 1)]

    for i in range(n - 1, -1, -1):
        # Set the first cell of the curr_row to 0 to set the base
        # case for this row. This is done by initializing the entire
        # row to 0
        curr_row = [0 for _ in range(cap + 1)]
        for c in range(1, cap + 1):
            # If the item 'i' fits in the current knapsack capacity,
            # the maximum value at d[i][c] is the largest of either:
            # 1. The max value if we include item 'i'
            # 2. The max value if we exclude item 'i'.
            if weights[i] <= c:
                curr_row[c] = max(values[i] + prev_row[c - weights[i]], prev_row[c])
            # If it doesn't fit, we have to exclude it
            else:
                curr_row[c] = prev_row[c]
        # Set the prev_row to curr_row values for the next iteration.
        prev_row = curr_row
    return prev_row[cap]


print("\n")
cap = 7
weights = [5, 3, 4, 1]
values = [70, 50, 40, 10]
print(f"Maxium value of good carried by a knapsack of capacity {cap} is: {knapsack(cap, weights, values)}")
print(f"Maxium value of good carried by a knapsack of capacity {cap} is: {knapsack_optimized(cap, weights, values)}")