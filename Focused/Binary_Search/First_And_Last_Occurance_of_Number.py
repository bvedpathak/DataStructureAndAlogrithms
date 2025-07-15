# The target many be duplicate so return the target's first and 
# last occurance
def first_and_last_occurance_of_a_number(nums, target):
    lower_bound = lower_bound_binary_search(nums, target)
    upper_bound = upper_bound_binary_search(nums, target)
    return [lower_bound, upper_bound]

def lower_bound_binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if nums and nums[left] == target else -1


def upper_bound_binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        # In upper-bound binary search, bias the midpoint to the right
        mid = (left + right) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid

    return right if nums and nums[right] == target else -1

print("\n")
nums = [1,2,3,4,4,4,5,6,7,8,9,10,11]
target = 4
print(f"Upper and Lower bounds for the {nums} for {target} are {first_and_last_occurance_of_a_number(nums, target)}")