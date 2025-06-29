## if string is aaabbccccd then the output should be a3b2c4d
## Assumption: string should only contain a-z or A-Z
def compress(str1):
    if str1 is None:
        return None
    
    if len(str1) < 3:
        return str1
    
    counter = 1
    result = []
    
    for i in range(1, len(str1)):
        if not str1[i-1].isalpha():
            raise ValueError("String is not an alphabet")
        if str1[i] != str1[i-1]:
            result.append(str1[i-1])
            if counter > 1:
                result.append(counter)
                counter = 1
            continue
        counter += 1

    result.append(str1[-1])
    if counter > 1:
        result.append(counter)
    
    return "".join(str(item) for item in result)

## The string decompression method for the above commpress function
def decompress(str1):
    if str1 is None:
        return None
    
    result = []
    for i in range(len(str1)):
        if str1[i].isalpha():
            result.append(str1[i])
        else:
            if i > 0:
                for j in range(int(str1[i])-1):
                    result.append(str1[i-1])
            else:
                raise ValueError("Incorrectly compress string")
    return "".join(result)

def test_compress():
    assert compress('aaaaabbbbcc') == 'a5b4c2'
    assert compress('a') == 'a'
    assert compress('abc') == 'abc'
    assert compress(None) == None
    assert compress('') == ''
    
try:
    test_compress()
except AssertionError as e:
    print(f"{e}: Test Cases failed")
except ValueError:
    print("Please check the input")

print("\n")
str1 = "aaaabc"
str2 = "a"
print(f"Compress string of {str1} is: {compress(str1)}")
print(f"De-Compress string of {str2} is: {decompress(str2)}")
print("\n")


        