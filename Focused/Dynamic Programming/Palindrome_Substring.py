def is_palindrome(input):
    if input is None:
        return False
    if len(input) < 2:
        return True
    
    i = 0
    j = len(input) - 1

    while i < j:
        if input[i] != input[j]:
            return False
        i += 1
        j -= 1
    return True

## Standard recurrsive way to go thru all possible combinations and find out 
## palindrome substrings within a string O(n3) time complexity i.e. O(n3) for 
## recurrsion multiply by another O(n) for palindrome check
def all_palindrome_substrings(input, i, j, result):
    if input is None or len(input) < 1:
        return result
    
    if j < i:
        return result
    
    if is_palindrome(input):
        result.add(input)
    
    result = all_palindrome_substrings(input[i+1:j], i+1, j, result)
    result = all_palindrome_substrings(input[i:j-1], i, j-1, result)
    
    return result

## Standard recurrsive way to get the longest palindrome (same like above just more efficient)
## due to the constraint in the problem statement
def longest_palindrome_substring(input, i, j, result):
    if input is None or len(input) < 2:
        return result
    
    if j < i:
        return result
    
    if len(input) < len(result):
        return result 
    
    if is_palindrome(input):
        result = input
        return result
    
    result = longest_palindrome_substring(input[i+1:j], i+1, j, result)
    result = longest_palindrome_substring(input[i:j-1], i, j-1, result)
    
    return result

## Longest Palindrome using Dynamic Programming
def longest_palindrome_substring_dp(input):
    n = len(input)

    if n < 2:
        return True
    longest_start = 0
    longest_end = 0
    palindrome_matrix = [[False for _ in range(n)] for _ in range(n)]

    for e in range(1, n):
        for s in range(e):
            is_inner_palindrome = palindrome_matrix[s+1][e-1] or (e - s) <= 2

            if input[s] == input[e] and is_inner_palindrome:
                palindrome_matrix[s][e] = True
                # Maintain the longest
                if e - s > longest_end - longest_start:
                    longest_start = s
                    longest_end = e

    return input[longest_start:longest_end+1]
  
input = 'geeksskeeg'
result = set()
print("\n\n")
print(f"Recurrsion: all palindrom substring combinations for {input} are: {all_palindrome_substrings(input, 0, len(input), result)}")
print("\n")
print(f"Recurrsion: Longest palindrom substring for {input} is: {longest_palindrome_substring(input, 0, len(input), "")}")
print("\n")
print(f"Dynamic Programming Way: Longest palindrom substring for {input} is: {longest_palindrome_substring_dp(input)}")
print("\n\n")
