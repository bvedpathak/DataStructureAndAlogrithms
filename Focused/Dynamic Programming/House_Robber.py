## The constraint is robber can not rob consecutive houses. So given that, 
## how much max money a robber can rob
## Standard recurrsive way of solving the optimization problem
## While space complexity is O(1), the time complexity will be O(n2)?
def rob(houses, i):
    if not houses:
        return 0
    if i < 0:
        return 0
    
    if i == 0:
        return houses[i]
    
    return (max(houses[i] + rob(houses, i-2), rob(houses, i-1)))

## Dynamic way of solving the same problem
## O(n) time complexity and O(n) space complexity  (not there is a more 
# optimized with using only two variabls instead of full dp)
def rob_dp(houses):
    if not houses:
        return 0
    
    if len(houses) == 1:
        return houses[0]
    
    result = [0 for _ in range(len(houses))]
    result[0] = houses[0]
    result[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        result[i] = max(houses[i] + result[i-2], result[i-1])

    return result[len(houses) - 1]    


houses = [1, 5, 3, 0, 9, 4]

print("\n\n")
print(f"Max money can be robbed using recurrsion: {rob(houses, len(houses) - 1)}")
print(f"Max money can be robbed using DP: {rob_dp(houses)}")
print("\n\n")



      
