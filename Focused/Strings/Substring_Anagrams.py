def substring_anagrams(str1, input):
    if len(input) > len(str1) or str1 is None or input is None:
        return None
    count = 0
    expected_feqs, window_freqs = [0] * 26, [0] * 26
    
    # Calculate the expected char frequency
    for c in input:
        expected_feqs[ord(c) - ord('a')] += 1

    left = right = 0
    while right < len(str1):

        window_freqs[ord(str1[right]) - ord('a')] += 1

        if len(input) == (right - left) + 1:
            if expected_feqs == window_freqs:
                count += 1
            window_freqs[ord(str1[left]) - ord('a')] -= 1
            left += 1
        right += 1

    return count

str1 = 'caabab'
input = 'aba'
print("\n")
print(f"Frequecy of the anagrams of the {input} in the string {str1} is: {substring_anagrams(str1, input)}")
print("\n")