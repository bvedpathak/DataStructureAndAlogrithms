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

print(replace_spaces("a bc "))