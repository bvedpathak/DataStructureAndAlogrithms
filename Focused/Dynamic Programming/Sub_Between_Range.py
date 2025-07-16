# Prefix Sum array is similar to DP array..
class SumBetweenRange:
    def __init__(self, nums):
        if not nums:
            self.prefix_sum = None
        else:
            self.prefix_sum = [nums[0]]
            for i in range(1, len(nums)):
                self.prefix_sum.append(self.prefix_sum[i-1] + nums[i])
    
    def sum_range(self, i, j):
        if j < i or j > len(self.prefix_sum):
            return None
        
        if i == 0:
            return self.prefix_sum[j]
        
        return self.prefix_sum[j] - self.prefix_sum[i-1]
    
print("\n")

nums = [3, -7, 6, 0, -2, 5]
range_obj = SumBetweenRange(nums)

i = 0
j = 3
print(f"Subrange for {nums} for the indexes i {i}, j {3} is: {range_obj.sum_range(i, j)}")

i = 2
j = 4
print(f"Subrange for {nums} for the indexes i {i}, j {3} is: {range_obj.sum_range(i, j)}")

i = 2
j = 2
print(f"Subrange for {nums} for the indexes i {i}, j {3} is: {range_obj.sum_range(i, j)}")
