# Function to evaluate expressions like 18 - (7 + (2 - 4) ) using stack
def evaluate_expression(str1):
    stack = []
    sign = 1
    result = 0
    curr_num = 0

    for c in str1:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == '+' or c == '-':
            result += curr_num * sign
            sign = -1 if c == '-' else 1
            curr_num = 0
        elif c == '(':
            stack.append(result)
            stack.append(sign)
            curr_num = 0
            sign = 1
        elif c == ')':
            result += curr_num * sign
            result *= stack.pop()
            result += stack.pop() 
            curr_num = 0
    return result + (curr_num * sign)
  
print("\n")
str1 = '18 - ( 7 + ( 2 - 4 ) )'
print(f"Result of the expression {str1} = {evaluate_expression(str1)}")
print("\n")