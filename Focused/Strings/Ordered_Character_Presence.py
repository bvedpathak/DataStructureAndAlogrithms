# Brute force algorithm with O(n*m) complexity with O(1) space complexity

def how_many_ordered_characters_v1(input_str, strs):
    if not input_str or not strs:
        return None
    
    final_count = 0
    for str1 in strs:
        i, j = 0, 0
        count = 0
        while i < len(input_str) and j < len(str1):
            if input_str[i] == str1[j]:
                j += 1
            i += 1
        final_count += 1 if j == len(str1) else 0
    return final_count

# Time: O(n *(len(repeated chars))), Space: O(n)
def how_many_ordered_characters_v2(input_str, strs):
    if not input_str or not strs:
        return None
    final_count = 0
    char_map = {}
    for i, chr in enumerate(input_str):
        lst = char_map.get(chr, [])
        lst.append(i)
        char_map[chr] = lst
    
    for str1 in strs:
        last_matched_char_index = -1
        for i, chr in enumerate(str1):
            if chr not in char_map or last_matched_char_index >= char_map.get(chr)[-1]:
                break
            else:
                for j in char_map.get(chr):
                    if j > last_matched_char_index:
                        last_matched_char_index = j
                        break
            if i == len(str1) - 1:
                final_count += 1
    return final_count

input_str = 'abcadceca'
strs = ['cad', 'cea', 'ca', 'aaa', 'zzz']
#strs = ['aaa', 'zzz']
print("\n")
print(f"How may substrings from the list {strs} present in {input_str}? {how_many_ordered_characters_v2(input_str, strs)}")
print("\n")
