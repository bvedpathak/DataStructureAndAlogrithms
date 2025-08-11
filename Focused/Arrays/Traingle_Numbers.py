# Consider a triangle composed of numbers where the top of the triangle is 1. Each subsequent
# number in the triangle is equal to the sum of three numbers above it: its top-left number, its
# top number, and its top-right number. If any of these three numbers don’t exist, assume they
# are equal to 0.
# Given a value representing a row of this triangle, return the position of the first even number
# in this row. Assume the first number in each row is at position 1.
# Time: O(1) Space: O(1)
def traingle_numbers(n):
    # If n is odd-numbered row, the first even number always starts at 
    # position of 2
    if n % 2 != 0:
        return 2
    # If n is a multiple of 4, the first even number always starts at 
    # position 3
    elif n % 4 == 0:
        return 3
    # For all other rows, the first even number always starts at 
    # position 4
    return 4

n = 4
print(f"\nThe first even number for the row {n} starts at the position: {traingle_numbers(n)}\n")
