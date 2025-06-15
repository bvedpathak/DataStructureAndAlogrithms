def find_digit_combinations(index, ans, lookup, permutation, digits):
    if digits is None or len(digits) < 1:
        return None
    if len(permutation) == len(digits):
        ans.append(permutation)
        return
        
    for chr in lookup.get(int(digits[index])):
        permutation += chr
        find_digit_combinations(index+1, ans, lookup, permutation, digits)
        permutation = permutation[:-1]
    return

def letter_combination_for_telephone_digits(digits):
    ans = []
    lookup = { 1: "   ",
               2: "abc",
               3: "def",
               4: "ghi",
               5: "jkl",
               6: "mno",
               7: "pqrs",
               8: "tuv",
               9: "wxyz"
    }

    find_digit_combinations(0, ans, lookup, "", digits)
    return ans


print("\n\n")
print(letter_combination_for_telephone_digits("23"))
print("\n\n")
