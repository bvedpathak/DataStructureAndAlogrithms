# Consider an example of multiple paranthesis types ([{}])
# Time: O(n), Space: O(1)
def paranthesis_balanced(str1):
    if str1 is None or len(str1) < 1:
        return None
    paranthesis_map = { '{': '}', '[': ']', '(': ')' }
    stack = []

    for c in str1:
        if c in paranthesis_map:
            stack.append(c)
        else:
            if c != paranthesis_map.get(stack[-1]):
                return False
            stack.pop()
    
    return len(stack) == 0

print("\n")
str1 = '()(({[]))[]'
print(f"Are paranthesis {str1} balanced? {paranthesis_balanced(str1)}")
print("\n")

