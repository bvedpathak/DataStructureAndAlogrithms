## Optimal solution 
## Time: O(n), Space: O(1)
def largest_container(nums):
    if nums is None:
        return None
    if len(nums) < 2:
        return 0
    start = 0
    end = len(nums) - 1
    max_units_of_water = 0
    while start < end: 
        max_units_of_water = max(max_units_of_water, min(nums[start], nums[end]) * (end - start))
        if nums[start] == min(nums[start], nums[end]):
            start += 1
        else:
            end -= 1
    return max_units_of_water

def test_largest_container():
    assert largest_container([]) == 0
    assert largest_container([1]) == 0
    assert largest_container([0, 1, 0]) == 0
    assert largest_container([3, 3, 3, 3]) == 9
    assert largest_container([1, 2, 3]) == 2
    assert largest_container([3, 2, 1]) == 2

print("\n")
container = [2, 7, 8, 3, 7, 6]

print(f"Largest Container for the given {container} is: {largest_container(container)}")

try:
    test_largest_container()
except AssertionError:
    print("Failed Test case(s) need attention")