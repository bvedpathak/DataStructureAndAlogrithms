def swap_odd_and_even_bits(n):
    even_mask = 0x55555555 #01010101010101010101010101010101
    odd_mask = 0xAAAAAAAA  #10101010101010101010101010101010

    even_bits = n & even_mask
    odd_bits = n & odd_mask
    # Shef the even bits to the left, the odd bits to the right, and merge the together
    return (even_bits << 1) | (odd_bits >> 1)


print("\n")
n = 41
print(f"Swapped odd/even bits for the original number of {n} becomes {swap_odd_and_even_bits(n)}")
