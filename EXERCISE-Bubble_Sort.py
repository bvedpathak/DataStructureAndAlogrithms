def bubble_sort(lst):
    count = len(lst)
    while count > 0:
        for i in range(count - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
        count -= 1
    return lst


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """