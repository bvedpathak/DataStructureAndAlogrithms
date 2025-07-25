# O(n log n) Time complexity and O(n) Space complexity
def group_anagrams(lst):
    if not lst:
        return [""]
    
    result = []
    lookup = {}
    
    for str in lst:
        sorted_str = "".join(sorted(str))
        if sorted_str in lookup:
            lookup.get(sorted_str).append(str)
        else:
            lookup[sorted_str] = [str]

    for lst in lookup.values():
        result.append(lst)

    return result

print("\n\n")
#print(group_anagrams(['abc', 'cab', 'ate', 'tae', 'cat', 'atc', 'eat', 'tea', 'nat', 'tan']))
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

print("\n\n")

