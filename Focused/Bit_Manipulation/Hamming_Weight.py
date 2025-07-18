# Hamming weights of integers is nothing but how many 1s in the binary
# representation of the given number. This problem is a DP problem around
# bitwise operators

def hamming_weights_of_integers(n):
    return [count_set_bits(x) for x in range(n + 1)]

def count_set_bits(x):
    count = 0
    # Count each set bit of 'x' unti 'x' equals 0

    while x > 0:
        # Increment the count if the LSB is 1
        count += (x & 1)
        # Right shift 'x' to shift the next bit to the LSB position.
        x >>= 1

    return count

print("\n")
n = 7
print(f"Number of 1s in the numbers till {n} are: {hamming_weights_of_integers(n)}")