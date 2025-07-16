# Given an array of integers, return an array Res so that res[i] is equal to the product of all
# the elements of the input array except the num[i] itself

# Approach 1 - Calculate the product of the entire array and then divide that product by num[i]
# so that the value would be product of the entire array except num[i]
# E.g. 
#    nums = [2, 3, 1, 4, 5] product of the whole array is 120
# so res  = [120/2, 120/3, 120/1, 120/4, 120/5]
def product_array_without_current_element_v1(nums):
    if not nums:
        return None
    entire_product = 1
    res = []
    for num in nums:
        entire_product *= num
    
    for num in nums:
        res.append(entire_product//num)

    return res

print("\n")

# Now if Interviewer says, obtain the similar results without using 'Division' operator then 
# we can think of a solution below where essentially the another logic to obtain the same is
# nums = [(2,    3),       1,      (4,      5)]
#.        L -> R product  (i)  *  R -> L product
#       nums = [2,  3,  1,  4,  5]
#       L->R = [1,  2,  6,  6, 24]
#.      R->L = [60, 20, 20, 5,  1]
#       Res  = [60, 40, 120,30, 24]
# For readability we can maintain L -> R product and R -> L product arrays but we can optimize 
# that in the result arrays itself with a running product..full code below
def product_array_without_current_element_v2(nums):
    res = [1] * len(nums)
    
    # First popluate the res with the running left product
    for i in range(1, len(nums)):
        res[i] = nums[i - 1] * res[i - 1]

    # Multiply the output with the running right product, from right to left
    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]

    return res

nums = [2, 3, 1, 4, 5]

print(f"Input {nums}, Result Array: {product_array_without_current_element_v1(nums)}")
print(f"Input {nums}, Result Array: {product_array_without_current_element_v2(nums)}")
