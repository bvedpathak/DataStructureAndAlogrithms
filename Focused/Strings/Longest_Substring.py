# Using O(n) time and space complexity. Below example is using a Set(). Same can be done using dictionary
# assuming reads are O(1)
def longest_substring(str):
    result = set()
    longest_substring = 0
    current_max = 0
    for chr in str:
        if chr in result:
            longest_substring = max(longest_substring, current_max)
            current_max = 0
            result = set()
        current_max += 1
        result.add(chr)
    return max(longest_substring, current_max)

## Exact same solution but using dictionary 
def longest_substring_v1(str):
    result = dict()
    longest_substring = 0
    current_max = 0
    for chr in str:
        if result.get(chr) == True:
            longest_substring = max(longest_substring, current_max)
            current_max = 0
            result = dict()
        current_max += 1
        result[chr] = True
    return max(longest_substring, current_max)
## Note the above ones may not work on a few strings because they toss away
# the whole string as soon as a single dup comes..Ideally we need to restart
# new string from the char next to dup charater

# The ideal solution is below which works for all the siutations. It is also called
# sliding window alogrithm
def longest_substring_v3(str):
    if len(str) <= 1:
        return len(str)
    result = dict()
    l = 0
    r = 0
    longest_substring = 0
    while r < len(str) and l < len(str):
        if str[r] in result:
            l = max(l, result.get(str[r]) + 1)
        result[str[r]] = r
        longest_substring = max(longest_substring, r - l+1)
        r += 1
    return(longest_substring)

print("\n\n")
print(longest_substring_v3("acdcecaf"))
print("\n\n")
