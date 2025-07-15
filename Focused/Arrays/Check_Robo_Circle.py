def is_circle_complete(steps):
    if not steps:
        return None
    x = y = 0
    for step in steps:
        if step == 'U':
            y += 1
        if step == 'D':
            y -= 1
        if step == 'L':
            x -= 1
        if step == 'R':
            x += 1
    return x == 0 and y == 0

print("\n\n")
print(is_circle_complete("UUDD"))
print(is_circle_complete("DRU"))
print("\n\n")

