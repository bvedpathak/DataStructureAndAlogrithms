import math
def reverse_32_bit_integer(n):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    reversed_n = 0
    # Keep looping until we have added all digits of 'n' to 'reversed_n'
    # in reverse order
    while n != 0:
        # digit = n % 10
        digit = int(math.fmod(n,10))
        # n = n // 10
        n = int(n / 10)
        # Check for integer overflow or underflow
        if (reversed_n > int(INT_MAX / 10)
            or reversed_n < int(INT_MIN / 10)):
            return 0
        # Add the current digit to 'reversed_n'
        reversed_n = reversed_n * 10 + digit
    return reversed_n

print("\n")
n = 12345
print(f"Reverse of an int {n} is: {reverse_32_bit_integer(n)}\n")
