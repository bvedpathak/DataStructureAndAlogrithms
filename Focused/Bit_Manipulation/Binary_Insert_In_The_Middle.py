def printable_bin(n):
    ## actual print version is: print(f"{bin(n)[2:]:0>16}")
    return "{:0>32}".format(bin(n)[2:])


def binary_insertion_within_bounds(n, m, i, j):
    if i > j:
        return 0
    
    mask = ((1 << i) - 1) | (32767 << j+1)
    shifted_m = m << i
    print(f"n           : {printable_bin(n)}")
    print(f"mask        : {printable_bin(mask)}")
    print(f"shifted m   : {printable_bin(shifted_m)}")
    
    return (n & mask) | shifted_m



n = 0b1000000000
i = 2
j = 6
m = 0b10011

print(printable_bin((n-1)))
print("\n")
print(f"Decimal: {n}, Binary: {printable_bin(n)}")
print(f"Decimal: {m}, Binary: {printable_bin(n)}")
print(f"Insertion Points: {i} {j}")
print("\n")
print(f"Final Answer: {printable_bin(binary_insertion_within_bounds(n, m, i, j))}")

'''
binary_number = 0b0001
temp = j
## Sort of traversing the binary bits of an integer 
while temp > 0:
    bit = temp & 1
    print(f"Bit: {bit}")
    temp = temp >> 1
'''

print("\n")

