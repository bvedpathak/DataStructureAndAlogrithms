def item_in_common(list1, list2):
    dict = {}
    for i in list1:
        dict[i] = True

    for i in list2:
        if dict.get(i):
            return True
    return False

def find_duplicates(list1):
    lookup = dict()
    result = []
    for i in list1:
        if lookup.get(i) and i not in result:
            result.append(i)
        else:
            lookup[i] = True
    return result

def first_non_repeating_char(str):
    hash_table = dict()
    for i in str:
        if i in hash_table.keys():
            hash_table[i] += 1
        else:
            hash_table[i] = 1
    for i in str:
        if hash_table.get(i) == 1:
            return i
    return None

def group_anagrams(list1):
    hash_table = dict()
    for str1 in list1:
        sorted_str = "".join(sorted(str1))
        if sorted_str in hash_table.keys():
            hash_table[sorted_str].append(str1)
        else:
            hash_table[sorted_str] = [str1]
    result = []
    for str1 in list1:
        sorted_str = "".join(sorted(str1))
        if sorted_str in hash_table.keys():
            result.append(hash_table.pop(sorted_str))
    return result

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))

"""
    EXPECTED OUTPUT:
    ----------------
    True

"""

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )

"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []
"""

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""