import random

class WeightedRandomSelection:
    def __init__(self, weights):
        self.prefix_sum = [weights[0]]
        for i in range(1,len(weights)):
            self.prefix_sum.append(self.prefix_sum[-1] + weights[i])

    def select(self):
        # Pick 
        target = random.randint(1, self.prefix_sum[-1])
        left, right = 0, len(self.prefix_sum) - 1

        while left < right:
            mid = (left + right) // 2

            if self.prefix_sum[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    
weights = [3, 1, 2, 4]

random_selector = WeightedRandomSelection(weights)

print("\n")

for _ in range(10):
    print(f"Random Number Selected from {weights} is {weights[random_selector.select()]}")

