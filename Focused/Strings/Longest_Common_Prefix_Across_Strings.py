# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_len = 200 # Since max length of a string can be 200 
    prefix = ""
    prev = strs[0]

    for i in range(1, len(strs)):
        curr = strs[i]
        j = 0
        while j < len(prev) and j < len(curr) and j < min_len:
            if prev[j] != curr[j]:
                break
            j += 1
        min_len = min(min_len, j)
        prefix = curr[:min_len]
        prev = curr

    return prefix if len(strs) > 1 else strs[0]

strs = ["flower","flow","flight"]

print(f"\nLongest Common prefix across all string is: {longest_common_prefix(strs)}\n")
