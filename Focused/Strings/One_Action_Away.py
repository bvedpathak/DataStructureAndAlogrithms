## Checks if exactly one char is removed from the original string
def is_a_char_removed(str1, str2):
    if str1 is None:
        return False
    
    if len(str1) - len(str2) != 1:
        return False
    diff = False
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if diff:
                return False
            diff = True
            i += 1
            continue
        i += 1
        j += 1
    
    return True

## Checks if exactly one char is replaced from the original string
def is_a_char_replaced(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) != len(str2):
        return False
    diff = False
    for i, chr in enumerate(str1):
        if str1[i] != str2[i]:
            if diff:
                return False
            diff = True
    return diff

## This is exactly one action taken on the orginal string i.e. either
## replaced a char, removed a char or inserted a char. The below function
## checks to see if there was such only one action taken or not
def one_away(str1, str2):
    if str1 is None and str2 is None:
        return False

    # If it is a replace char case
    if len(str1) == len(str2):
        return is_a_char_replaced(str1, str2)
    
    # If it is a removed char case
    if len(str1) - len(str2) == 1:
        return is_a_char_removed(str1, str2)

    # If it is an insert char case
    if len(str2) - len(str1) == 1:
        return is_a_char_removed(str2, str1)

    return False

def test_one_away_insert():
    assert one_away('pale', 'pales')
    assert not one_away('pale', 'paless')

def test_one_away_replace():
    assert one_away('pale', 'bale')
    assert not one_away('pale', 'b le')

def test_one_away_removed():
    assert one_away('pale', 'ple')
    assert not one_away('pale', 'al')

print("\n")

str1 = 'pale'
str2 = 'ple'
print(f"is string {str2} is one action away from  {str1}? {one_away(str1, str2)}")
print("\n")

try:
    test_one_away_insert()
    test_one_away_replace()
    test_one_away_removed()
except AssertionError:
    print("Test Cases failed..")