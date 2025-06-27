## Standard ALL permutations recursive function
def permulations_recursive(s):

    if len(s) == 0:
        return []
    
    permutations = [""]

    for i in range(len(s)):
        chr = s[i]
        remaining_chars = s[:i] + s[i+1:]
        for p in permulations_recursive(remaining_chars):
            permutations.append(chr + p)
    return permutations

## Check if both are combination of each other
## Option - 1 Sort both the string and compare and return
## Time O(n log n), Space O(1)
def permutation_check_using_sort(str1, str2):
    return sorted(str1) == sorted(str2)

## Option - 2 Maintain the ASCII map and compare the counts
## Assumption: ASCII string
## Time O(n), Space O(1)
def permutation_check_using_counts(str1, str2):

    lookup = [0] * 128 ## counts for all 128 ASCII chars

    ## Maintain count for each char in string 1
    for chr in str1:
        lookup[ord(chr)] += 1
    
    ## Substract count for each char in string 2
    for chr in str2:
        lookup[ord(chr)] -= 1

    ## Result should be zero 
    for i in range(len(lookup)):
        if lookup[i] != 0:
            return False
    return True

print("\n")
print(permulations_recursive('abc'))
print(permutation_check_using_counts("abcd", "dca"))
print("\n")
