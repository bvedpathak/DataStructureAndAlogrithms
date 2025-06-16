def is_palindrome(str):
    if str is None or len(str) < 1:
        return False
    i = 0
    j = len(str) - 1

    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    
    return True

def palindrome_substrings(str, curr, ans, index):

    if str is None or len(str) < 1:
        return 
    
    if index >= len(str):
        return
    
    for i in range(index, len(str)):
        curr += str[i]
        if is_palindrome(curr):
            ans.append(curr)
        palindrome_substrings(str, curr, ans, i+1)
        curr = curr[:-1]
    return

ans = []
str = "kadak"

print("\n\n")
palindrome_substrings(str, "", ans, 0)
print(f"All palindrome substrings for {str} are: {ans}")
print(f"Unique combinations are: {set(ans)}")
print("\n\n")
