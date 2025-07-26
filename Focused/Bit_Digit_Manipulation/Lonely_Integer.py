# Find the only Non-duplicate integer in the array
def lonely_integer(nums):
    res = 0
    # XOR each element of the array so that duplicate values will cancel
    # each other out (x ^ x = 0)
    for num in nums:
        res ^= num
    # res will store the lonely integer because if would not have been
    # cancelled out by any duplicate
    return res

print("\n")
nums = [1, 3, 3, 2, 1]

print(f"The non-duplicate integer in the array {nums} is: {lonely_integer(nums)}")