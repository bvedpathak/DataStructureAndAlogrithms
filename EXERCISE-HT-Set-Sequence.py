def longest_consecutive_sequence(list):
    lookup = set()
    for num in list:
        lookup.add(num)
    maximum = 0
    for num in list:
        curr_max = 1
        while True:
            if curr_max > maximum:
                maximum = curr_max
            if num + 1 in lookup:
                curr_max += 1
                num += 1
            else:
                break
    return maximum

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

print(longest_consecutive_sequence([9]))

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""