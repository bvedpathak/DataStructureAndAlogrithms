## A function to determine if a string has all unique chars
## Time: O(n), Space: O(n)
def unique_check_with_datastructure(str1):
    lookup = set()
    for chr in str1:
        if chr in lookup:
            return False
        lookup.add(chr)
    return True

## A Brute Force way to determine if a string has all unique chars (w/o using extra space)
## Time: O(n2), Space: O(1)
def unique_check_without_datastructure(str1):
    for i in range(len(str1)):
        for j in range(i+1, len(str1)):
            if str1[i] == str1[j]:
                return False
    return True


## A better way to determine if a string has all unique chars (w/o using extra space)
## Time: O(n.log n), Space: O(1)
def unique_check_without_datastructure_optimal(str1):
    str1 = sorted(str1)
    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            return False
    return True

## An optimized way to determine if a string has all unique chars (w/o using extra space)
## Time: O(n), Space: O(1)
## Assumption: Input will be ASCII which is max 128 chars so we can have a constant 128 char
## lookup array regardless of the input size i.e. constant space that is O(1)
def unique_check_without_datastructure_ascii(str1):
    lookup = [False] * 128 ## Max 128 ascii chars can be there so O(128) i.e. O(1)
    for chr in str1:
        val = ord(chr)
        if lookup[val] == True:
            return False
        lookup[val] = True
    return True

print("\n")
print(f"Does the string contain unique chars? {unique_check_with_datastructure("this")}")
print(f"Does the string contain unique chars? {unique_check_without_datastructure("this")}")
print(f"Does the string contain unique chars? {unique_check_without_datastructure_optimal("tg")}")

'''
for chr in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
    print(f"char {chr}: Unicode: {ord(chr)}")

'''