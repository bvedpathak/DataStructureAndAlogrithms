# Time: O(n2), Space: O(1)
def bubble_sort(lst):
    count = len(lst)
    while count > 0:
        for i in range(count - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        count -= 1
    return lst

print(bubble_sort([3,4,5,6,1,2,3]))
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """