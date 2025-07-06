
def longest_uniform_substring_after_replacements(str1, k):
    freqs = {}
    left = right = 0
    highest_freqs = max_len = 0
    while right < len(str1):
        # Update the frequency of the character at the right pointer
        # and the highest frequency for the current window.
        freqs[str1[right]] = freqs.get(str1[right], 0) + 1
        highest_freqs = max(highest_freqs, freqs[str1[right]])
        # Calculate the replacements needed for the current window
        num_chars_to_replace = (right - left + 1) - highest_freqs
        # Slide the window if the number of replacements needed exceeds
        # 'k'. The right pointer always get advanced, so we just need
        # to advance the 'left'
        if num_chars_to_replace > k:
            # Remove the char at the lft pointer from the hash map
            # before advancing the left pointer
            freqs[str1[left]] -= 1
            left += 1
        # Since the length of the current window increases or stays the 
        # same, assign the length of the current window to 'max-len'.
        max_len = right - left + 1
        right += 1
    return max_len    

print("\n")
str1 = 'aabcdcca'
k = 2
print(f"Max length of the uniform string by replacing {k} characters can be achieved is {longest_uniform_substring_after_replacements(str1, k)}")

