# Below is the algorithm without using stack but just achieving the result
# using 2 for loops
# Time: O(n2), Space: O(1)
def larest_number_to_the_right_v1(input):
    if not input:
        return None
    result = [-1] * len(input)

    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[j] > input[i]:
                result[i] = input[j]
                break
    return result

# Below is slightly more efficient algorithm but trading off with space
# Time: O(n) but Space: O(n)
def larest_number_to_the_right_v2(input):
    if not input:
        return None
    
    result = [-1] * len(input)
    stack = []

    for i in range(len(input) - 1, -1, -1):
        while stack and stack[-1] <= input[i]:
            stack.pop()
        
        result[i] = stack[-1] if stack else -1
        stack.append(input[i])

    return result

print("n")
input = [1, 1, 1, 1, 1]
print(f"Largest Num to the right for {input} are {larest_number_to_the_right_v1(input)}")
print(f"Largest Num to the right for {input} are {larest_number_to_the_right_v2(input)}")