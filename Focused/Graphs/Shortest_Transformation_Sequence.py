# Given two words, start and end, and a list containing words, return the 
# length of the shortest transformation sequence to tranform start to end.
# A transformation sequence is a series of words in which:
# - Each word differs from the preceding word by exactly one letter.
# - Each word in the ssequence exists in the input list
# If no such transformation sequence exists, return 0
# s = red and e = hit
# input list = ["red", "bed", "hat", "rod, "rad", "rat", "hit", "bad", "bat"]
# output = 5
# how? red -> rad -> rat -> hat -> hit
# Constraints:
# - All words of same length
# - All words contain only lowercase English letters
# - The input list contains no duplicate words
# Time: O(L.n2) where L is the length of the word and n is number of words
# This is single sided s -> e BFS traversal but we can optimize this using
# bi-directional BFS starting from e -> s as well and meeting in the middle

from collections import deque
def shortest_transformation_sequence(s, e, input_list):
    if not s or not e or not input_list:
        return 0
    # s and e are already same then return right away
    if s == e:
        return 1
    
    visited = set()
    q = deque()
    q.append(s)
    visited.add(s)
    dist = 0

    # Use level-order traversal to find the shortest path from the start
    # word to the end word
    while q:
        dist += 1
        # Process current level from the q. Remember, range(len(q)) is 
        # one time fetch as wont change as we add more elements into the 
        # queue inside the loop (this is the main key here)
        for _ in range(len(q)):
            curr = q.popleft()
            # If we found the end word, we have reached it via the shortest
            # path
            if curr == e:
                return dist
            # Gather all the one-replace-away words from the input list and
            # add to the queue. Ignore of the word is already visited
            for next_word in input_list:
                if next_word not in visited and one_replace_away(curr, next_word):
                    q.append(next_word)
                    visited.add(next_word)
    # If we reached here means we looked at all inputs and did not reach to
    # the end word so return 0
    return 0

def one_replace_away(curr, target):
    if len(curr) != len(target):
        return False
    
    i, j = 0, 0
    one_off = False
    while i < len(curr):
        if curr[i] != target[j]:
            # Forgive one mismatch but bail if more than 
            # one found
            if not one_off:
                one_off = True
            else:
                return False    
        j += 1
        i += 1
    
    return one_off

print("\n")
s = 'red'
e = 'hit'

input_list = ['red', 'bed', 'hat', 'rod', 'rad', 'rat', 'hit', 'bad', 'bat']

print(f"Shortest Path to reach from {s} to {e} is: {shortest_transformation_sequence(s, e, input_list)}")

