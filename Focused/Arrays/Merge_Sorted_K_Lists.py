# Solution using two pointers method with O(n) time complexity
def merge_two_sorted_lists(lst1, lst2):
    if lst1 is None or len(lst1) < 1:
        return lst2 
    l1 = 0
    l2 = 0
    result = []
    while l1 < len(lst1) and l2 < len(lst2):
        if lst1[l1] < lst2[l2]:
            result.append(lst1[l1])
            l1 += 1
        else:
            result.append(lst2[l2])
            l2 += 1

    while l1 < len(lst1):
        result.append(lst1[l1])
        l1 += 1

    while l2 < len(lst2):
        result.append(lst2[l2])
        l2 += 1

    return result

# Iterative way of merging
def merge_k_sorted_lists(input_list):
    ans = []
    for lst in input_list:
        ans = merge_two_sorted_lists(ans, lst)
    return ans

# Recurrsive way of merging
def merge(input_list):
    if input_list is None or len(input_list) < 1:
        return None
    if len(input_list) == 1:
        return input_list[0]
    
    return merge_two_sorted_lists(merge(input_list[:len(input_list)//2]), merge(input_list[len(input_list)//2:]))

print("\n\n")
print(merge([[1,2,3], [2,3,4,5], [4,8,10]]))
print("\n\n")

