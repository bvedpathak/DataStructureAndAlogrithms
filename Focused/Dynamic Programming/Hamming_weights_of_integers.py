# Hamming weights of integers is nothing but how many 1s in the binary
# representation of the given number. This problem is a DP problem around
# bitwise operators

def hamming_weights_of_integers_dp(n):
    # Base case: The number of set bits in 0 is just 0. We set dp[0] to 0
    # by initializing the entire DP array to 0.
    dp = [0] * (n + 1)

    for x in range(1, n + 1):
        # dp[x] is obtained using the result of dp[x >> 1] plus the LSB of 'x'
        dp[x] = dp[x >> 1] + (x & 1)
    
    return dp

print("\n")
n = 7
print(f"Hamming weight for all numbers including {n} is: {hamming_weights_of_integers_dp(n)}")