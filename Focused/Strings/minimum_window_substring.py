def is_a_substr(lookup, outcome):
    if len(lookup) != len(outcome):
        return False
    for k, v in lookup.items():
        if outcome.get(k) < v:
            return False
    return True

def still_a_substr(chr, lookup, outcome):
    if chr not in outcome:
        return False
    if outcome.get(chr) < lookup.get(chr):
        return False
    return True

def min_window_substr(input_str, str):
    if input_str is None or str is None or len(input_str) < 1 or len(str) < 0:
        return []
    b = 0
    e = 0
    min_substr_len = len(input_str)
    result = []

    lookup = {}
    outcome = {}

    # Populate the Lookup map
    for chr in str:
        if chr in lookup:
            lookup[chr] = lookup.get(chr) + 1
        else:
            lookup[chr] = 1
    
    while e < len(input_str):
        temp_str = [b, e]
        if input_str[e] in lookup:
            
            if input_str[e] in outcome:
                outcome[input_str[e]] = outcome.get(input_str[e]) + 1
            else:
                outcome[input_str[e]] = 1
            
            if is_a_substr(lookup, outcome):
                if min_substr_len > e - b:
                    min_substr_len = e - b
                    result = [b, e]
                while b < e and b < len(input_str):
                    curr_b = input_str[b]
                    if curr_b in outcome:
                        if outcome.get(curr_b) <= 1:
                            del outcome[curr_b]
                        else:
                            outcome[curr_b] = outcome.get(curr_b) - 1
                        if not still_a_substr(curr_b, lookup, outcome):
                            b += 1
                            break
                    b += 1
                    if min_substr_len > e - b:
                        min_substr_len = e - b
                        result = [b, e]
        e += 1
    return result
    

print("\n\n")
print(min_window_substr("amplewatersupplyars", "ars"))
print("\n\n")
