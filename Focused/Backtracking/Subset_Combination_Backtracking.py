def add_to_answer_and_repeat(nums, ans, curr, index):
    if index > len(nums):
        return
    
    # Add list to the result
    ans.append(curr[:])
    
    for i in range(index, len(nums)):
        curr.append(nums[i])
        add_to_answer_and_repeat(nums, ans, curr, i+1)    
        curr.pop()
    return

def find_all_subsets(nums):
    ans = []
    add_to_answer_and_repeat(nums, ans, [], 0)
    return ans

print("\n\n")
print(find_all_subsets([4, 5, 6]))
print("\n\n")
