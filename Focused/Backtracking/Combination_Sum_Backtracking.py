def combination_sum(nums, target, ans, curr, curr_sum, index):
    if not nums:
        return 
    
    if curr_sum == target:
        ans.append(curr[:])
    elif curr_sum < target: 
        for i in range(index, len(nums)):
            curr.append(nums[i])
            combination_sum(nums, target, ans, curr, curr_sum+nums[i], i)
            curr.pop()
    return

ans = []
nums = [2,3,6]
target = 8

print("\n\n")
combination_sum(nums, target, ans, [], 0, 0)
print(f"Combinations adding up to the {target} are: {ans}")
print("\n\n")

'''
            
                2                       3                       6
            2       
        2   3   6
    2   3(x)    6(x)
        6(x)

'''