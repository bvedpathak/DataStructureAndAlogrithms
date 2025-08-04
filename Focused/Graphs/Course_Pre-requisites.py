# Given an integer n representing the number of courses lebeled from 0 to n - 1, and
# an array of prerequisites pairs, determine if it's possible to entroll in all courses
# Each prerequsite is represented as a pair [a, b], indicating that course a must be 
# taken before course b
from collections import defaultdict, deque
def pre_requisites(n, prerequisites):
    graph = defaultdict(list)
    in_degrees = [0] * n

    # Represent the graph as an adjacency list and record the in-degree of each course
    for prerequisite, course in prerequisites:
        graph[prerequisite].append(course)
        in_degrees[course] += 1

    queue = deque()
    # Add all courses with an in-degree of a 0 to the queue
    for i in range(n):
        if in_degrees[i] == 0:
            queue.append(i)
    
    enrolled_courses = 0

    # Perform topological sort
    while queue:
        node = queue.popleft()
        enrolled_courses += 1
        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            # If the in-degree of a neighboring course becomes 0, add
            # it to the queue
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)
    # Return ture if we've successfully enrolled in all courses
    return enrolled_courses == n


print ("\n")
n = 6 # n - 1 courses
prerequisites = [[0, 1], [0, 2], [3, 2], [1, 4], [2, 4], [4, 5]]

print(f"Can all the {n} courses to be enrolled without cycles? {pre_requisites(n, prerequisites)}")