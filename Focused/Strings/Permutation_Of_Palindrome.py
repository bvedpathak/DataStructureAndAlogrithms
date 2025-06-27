## Check if a given string is a permutation of a palindrome
## Characteristics of a palindrome are
## 1. The odd length strings will have even count of all unique characters except one (the middle one)
## 2. The even lenght string will have even count of all unique characters
## 3. Do not consider spaces and non-letter characters 
## 4. Capitalization does not matter
## Time O(n) Space O(n)
def is_palindrome_permutation(str1):
    if str1 is None or len(str1) < 1:
        return False
    
    lookup = {}
    count_non_letter_chars = 0
    for chr in str1:
        if chr.isalpha():
            lookup[chr.lower()] = lookup.get(chr.lower(), 0) + 1
        else:
            count_non_letter_chars += 1

    count_odds = 0
    for v in lookup.values():
        if v % 2 != 0:
            count_odds += 1
    if (len(str1) - count_non_letter_chars) % 2 != 0:
        return True if count_odds == 1 else False
    return True if count_odds == 0 else False



print("\n")
print(is_palindrome_permutation('k a da k'))
print("\n")

## Sample Test case
def test_is_palindrome_permutation():
    result = is_palindrome_permutation("k a d a k")
    assert result == True

## Calling the test case 
try:
    test_is_palindrome_permutation()
except AssertionError:
    print("First Test Case Failed")

