# Determine the highest possible setting of the woodcutter(H)
# so that it cuts aleast k meters of wood. The hight of the trees
# is given by the numbers in the list and a value k representing the
# total length of wood that needs to be cut
def highest_possible_height(trees, k):
    if not trees:
        return 0
    
    # we will use Binary search on possible height settings to determine
    # the appropriate height
    bottom = 0
    
    # Find the tallest tree and store
    top = max(trees)

    # Search binary search way on different H settings
    while bottom < top:
        ## Bias the midpoint toward top since we need to give woods equal or
        ## more than the k
        mid = (bottom + top) // 2 + 1
        wood = 0
        for num in trees:
            if num > mid:
                wood += num - mid
        if wood >= k:
            bottom = mid
        else:
            top = mid - 1
    return top

print("\n")
trees = [2, 6, 3, 8]
k = 2
print(f"The H should be set to {highest_possible_height(trees, k)}")
