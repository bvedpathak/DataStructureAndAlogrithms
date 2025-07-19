# The four sum is leading to zero
def four_sum_count(a, b, c, d):
    result = {}
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] + b[j] in result:
                result[a[i] + b[j]] = result.get(a[i] + b[j], 0) + 1
            else:
                result[a[i] + b[j]] = 0

    for i in range(len(c)):
        for j in range(len(d)):
            if 0 - c[i] + d[j] in result:
                result[0 - c[i] + d[j]] = result.get(0 - c[i] + d[j]) + 1
    
    for k, v in result.items():
        print(f"k: {k}, v: {v}")

print("\n\n")
print(four_sum_count([1,2,4,5], [1,2,-1,3], [-1, -2, 3, 4], [-1,-2,-3,-4]))
print("\n\n")

