# Using set to add values first and then checking the size of the
# set at the end
def contains_duplicate(nums):
    lookup = set()
    for num in nums:
        if num in lookup:
            return True
        lookup.add(num)
    return False

# Using Maps to add values and return as soon a duplicate key comes in
def contains_duplicate_v1(nums):
    lookup = dict()
    for num in nums:
        if num in lookup:
            return True
        lookup[num] = True
    return False

print("\n\n")
print(contains_duplicate([1,2,3,4,5,5,6]))
print(contains_duplicate_v1([1,2,3,4,5,6]))
print("\n\n")



