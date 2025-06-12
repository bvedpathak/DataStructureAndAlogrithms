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

print("\n\n")
print(merge_two_sorted_lists([1,2,3], [2,3,4,5]))
print("\n\n")

