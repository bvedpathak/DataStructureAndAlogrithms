## DP way of calculating trapped rained water
## To simplify assume the BASE formula i.e. water = min(side two walls) - height of the center
def total_trapped_rain_water(height):
    if height is None or len(height) < 2:
        return 0
    
    left_max = [0] * len(height)
    right_max = [0] * len(height)
    water = 0
    # First calculate the tallest building see so far in the left
    left_max[0] = height[0]
    for i in range(1, len(left_max)):
        left_max[i] = max(height[i], left_max[i-1]) # which wall is hieghted, the one seen till now or the current one

    # Then calculate the tallest building see so far in the right
    right_max[-1] = height[-1]
    for i in range(len(right_max)-2, 0, -1):
        right_max[i] = max(height[i], right_max[i+1]) # which wall is hieghted, the one seen till now or the current one

    for i in range(1,len(height)-1):
        water += min(left_max[i], right_max[i]) - height[i]

    return water

height = [1,0,2,1,0,1,3]
print("\n\n")
print(f"Max water can be trapped is: {total_trapped_rain_water(height)}")
print("\n\n")
