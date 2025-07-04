## Helper function to get the sum if squares of the individual numbers
def get_next_num(num):
    next_num = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        next_num += digit ** 2
    return next_num

## Happy number is the one whoes squares of individuals digits eventually sum up to 1
def is_a_happy_number(num):
    fast = num
    slow = num
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))

        if fast == 1:
            return True
        
        if fast == slow:
            return False

print("\n")
num = 123
print(f"is {num} a happy number? {is_a_happy_number(num)}")
