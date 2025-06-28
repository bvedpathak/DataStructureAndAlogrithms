## Replace each occurance of the space with %20 (URLify)
def replace_spaces(str1):
    ## the in-built function return str1.replace(' ', '%20')
    space_count = str1.count(' ')
    if space_count == 0:
        return str1
    
    new_string = ''
    
    for old_index in range(len(str1)):
        if str1[old_index] == ' ':
            new_string += '%20'
        else:
            new_string += str1[old_index]

    return new_string

## str1 = 'waterbottle' str2 = 'etbottlewat'
## we only have one call of isSubstring available to make in order to
## figure out if it is a rotation. 
## Solution: str1 = <xy> e.g. str2 = <yx> so s1+s1 ie. xyxy will always have 
## <yx> as a substring e.g. 'waterbottlewaterbottle' has 'erbottlewat' as a 
## substring i.e. 'wat<erbottlewat>erbottle
def string_rotation_check(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) != len(str2):
        return False
    return str2 in (str1+str1)

print("\n")
#print(string_rotation_check('waterbottle', 'erbottlewat'))
#print(replace_spaces("a bc "))
#print(is_a_char_removed('', ''))
#print(is_a_char_replaced('a', 'bc'))
print("\n")