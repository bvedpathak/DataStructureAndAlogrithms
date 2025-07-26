def repeated_removal_of_adjacent_duplicates(input_str):
    if not input_str:
        return None
    
    stack = []
    for chr in input_str:
        # If the current character is the same as the top character on the stack,
        # a pair is adjacent duplicates has been formed. So pop the char from the 
        # stack 
        if stack and stack[-1] == chr:
            stack.pop()
        else:
        # Otherwise, push the current character onto the stack
            stack.append(chr)
    # Return the remaining characters as s string
    return "".join(stack)

print("\n")
input_str = 'aacabba'

print(f"String {input_str} after repeated removing the adjacent duplicates is: {repeated_removal_of_adjacent_duplicates(input_str)}\n")