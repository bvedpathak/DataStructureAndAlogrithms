# O(n) Time complexity and O(n) Space complexity
def group_anagrams(lst):
    result = []
    lookup = {}
    if lst is None or len(lst) < 1:
        return [""]
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
print(group_anagrams(['abc', 'cab', 'ate', 'tae', 'cat', 'atc', 'eat', 'tea', 'nat', 'tan']))
print("\n\n")

