def add_to_answer_and_repeat(index, curr, ans, nums):
    if index > len(nums):
        return
    
    # Add list to the list
    ans.append(curr[:])
    
    for i in range(index, len(nums)):
        curr.append(nums[i])
        add_to_answer_and_repeat(i+1, curr, ans, nums)    
        curr.pop()
    return

def find_all_subsets(nums):
    ans = []
    add_to_answer_and_repeat(0, [], ans, nums)
    return ans

print("\n\n")
print(find_all_subsets([1]))
print("\n\n")
