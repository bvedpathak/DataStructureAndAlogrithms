# Distribute candies among the students sitting in a row following the two rules below:
# 1. Each student will get atleast 1 candy
# 2. If a neighboring student has more rating then that student gets more candies than the lower
#    rating candidate
def optimal_candy_distribution(ratings):

    # Ensure each child starts with 1 candy    
    candies = [1] * len(ratings)

    # First Pass: For each child, ensure the child has more candies than their left-side
    # neighbor if the current child's rating is higher
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Second Pass: For each child, ensure the child has more candies than their right-side
    # neighbor if the current child's rating is higher
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            # If the current child already has more candies than their 
            # right side neighbor, keep the higher amount else give one more
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)

print("\n")
ratings = [4, 3, 2, 4, 5, 1]

print(f"The optimal candies can be distributed given the contraints are: {optimal_candy_distribution(ratings)}")
