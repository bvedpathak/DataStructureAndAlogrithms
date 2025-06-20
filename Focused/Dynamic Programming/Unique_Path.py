# Standard recurrsive function to get all possible paths
# Note: with a minor modification, you can maintain and get an optimal path
# Top down approach
def all_paths(start, target, moves, result):
    if start is None or len(start) < 2:
        return result
    if target is None or len(target) < 2:
        return result
    
    if start == target:
        result.append(moves[:])
        return result
    
    ## Down Direction
    if start[0] < target[0]:
        start[0] += 1
        moves.append('D')
        result = all_paths(start, target, moves, result)
        moves.pop()
        start[0] -= 1
    
    ## Right Direction
    if start[1] < target[1]:
        start[1] += 1
        moves.append('R')
        result = all_paths(start, target, moves, result)
        moves.pop()
        start[1] -= 1
    return result

## The total paths using DP (it gives just the number of paths not the actual paths)
## Bottom up approach
def all_paths_using_dp(start, target):
    if start is None or target is None or len(start) < 2 or len(target) < 2:
        return []
    dp = [[0 for x in range(target[0]+1)] for y in range(target[1]+1)]
    
    ## Only one vertical move exists 
    for i in range(target[0]+1):
        dp[i][0] = 1

    ## Only one horizontal move exists
    for i in range(target[1]+1):
        dp[0][i] = 1

    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[target[0]][target[1]]

start =[0,0]
target = [3,3]
result = all_paths(start, target, [], [])
print("\n\n")
print(f"All possible ways to reach to the target {target} are: {result}, Total: {len(result)}")
print("\n\n")
print(f"Using DP: possible ways to reach to the target {target} are: , Total: {all_paths_using_dp(start, target)}")
print("\n\n")

