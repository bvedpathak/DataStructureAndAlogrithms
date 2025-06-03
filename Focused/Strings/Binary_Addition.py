def add_binary_strings(str1, str2):
    carry = 0
    i = len(str1) - 1
    j = len(str2) - 1
    result = ''
    while i >= 0 or j >= 0 or carry == 1:
        digit1 = '0'
        digit2 = '0'
        if i >= 0:
            digit1 = str1[i]
        if j >= 0: 
            digit2 = str2[j]
        result = str((int(digit1)+int(digit2) + carry)%2) + "" + result
        carry =  (int(digit1)+int(digit2) + carry)//2
        j -= 1
        i -= 1

    return result

print("\n\n")
print(add_binary_strings("1111", "1111"))
print("\n\n")
