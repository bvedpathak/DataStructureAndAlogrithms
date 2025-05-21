def merge(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    result = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1
            result.append(list2[j])
            j += 1

    if not (i == len(list1) and j == len(list2)):
        if i == len(list1):
            result.extend(list2[j:])
        else:
            result.extend(list1[i:])
    return result

# MERGE REQUIRES TWO SORTED LISTS:
#print(merge([1,2,7,8], [3,4,5,6]))
print(merge([1,2,7,8], None))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """