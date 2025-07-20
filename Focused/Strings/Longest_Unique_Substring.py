# The below method uses dynamic sliding window technique to find 
# longest unique substring using two points by dynamically incrementing
# them
# Time: O(n), Space: O(n)
def longest_unique_substring(str1):
    if str1 is None:
        return 0
    
    left = right = 0
    max_substring = 0
    lookup = dict()

    while right < len(str1):
    
        if str1[right] in lookup and lookup[str1[right]] >= left:
            left = lookup.get(str1[right]) + 1
    
        lookup[str1[right]] = right
    
        max_substring = max(max_substring, right - left + 1)
        right += 1

    return max_substring


str1 = "abccdef"
print("\n")
print(f"Longest Unique Character Substring for the string {str1} is: {longest_unique_substring(str1)}")
print("\n")