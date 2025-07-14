# You are given a 2D array making 0s and 1s where 1 indicates a farm land
# you are job is to return the maximum farmable land (in square shape only)
def max_squared_farming_land(farm):
    if not farm:
        return None
    
    rows = len(farm)
    cols = len(farm[0])
    
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    max_land = 0

    for i in range(1, rows):
        for j in range(1, cols):
            # Check if my surrounding 3 directions i.e. Top, Left and Upper Diagonal is 1 and mark in dp
            if farm[i][j] == 1 and farm[i-1][j] == 1 and farm[i-1][j-1] == 1 and farm[i][j-1] == 1:
                dp[i][j] = 1
                # only add cummulative squares if all surrounding DPs show > 0
                if dp[i-1][j] > 0 and dp[i][j-1] > 0 and dp[i-1][j-1] > 0:
                    dp[i][j] += dp[i-1][j-1]
                max_land = max(max_land, dp[i][j])
    
    return max_land + 1 if max_land > 0 else 0

farm = [ [ 0, 0, 1, 1, 1],
         [ 0, 0, 1, 1, 1],
         [ 0, 0, 1, 0, 1],
         [ 0, 0, 0, 1, 1]
]

print("\n")
print(f"Max squared farm land is: {max_squared_farming_land(farm)}")
print("\n")
