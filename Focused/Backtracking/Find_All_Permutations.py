def backtrack(nums, used, curr, res):
    if not nums:
        return 
    
    if len(curr) == len(nums):
        res.append(curr[:])

    for num in nums:
        if num not in used:
            curr.append(num)
            used.add(num)
            backtrack(nums, used, curr, res)
            curr.pop()
            used.remove(num)
    return

def find_all_permutations(nums):
    res = []
    backtrack(nums, set(), [], res)
    return res

print("\n")
nums = [4, 5, 6]
print(f"All permulations of the {nums} are: {find_all_permutations(nums)}")
