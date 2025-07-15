import math

## The below method is not a part of the optimal solution but given just
## for the reference on how to check if a single number is prime or not
def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False
    # Check for factors from 2 up to the square root of num
    # We only need to check up to the square root because if a number
    # has a factor greater than its square root, it must also have
    # a factor smaller than its square root.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a factor, so it's not prime
    return True  # No factors found, so it's prime

## Optimial Solution - O(n)
def count_and_return_primes(nums):
    result_map = {num: True for num in nums}
    result_map[0] = False
    result_map[1] = False
    max_num = max(nums)
    n = int(math.sqrt(max_num)) ## Important to keep in mind
    for i in range(2, n):
        try:
            if result_map[i]:
                for multiple_of_i in range(i*2, max_num, i):
                    result_map[multiple_of_i] = False
        except KeyError:
            print("Key Not Found")
    # Gather the numbers that are still True (means prime) and 
    # return them
    list_of_primes = []
    for k, v in result_map.items():
        if v == True:
            list_of_primes.append(k)
    
    return list_of_primes

print(f"List of Primes: {count_and_return_primes([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])} ")
