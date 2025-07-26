def spiral_matrix(matrix):
    if not matrix:
        return []
    result = []

    # Initialize the matrix boundaries.
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    # Outer loop of traversal until all elements are visited 
    while top <= bottom and left <= right:
        # Move from left to right along the top boundary
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Move from top to bottom along the right boundary
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Check that the bottom boundary has not passed the top boundary
        # before moving from right to left along the bottom boundary
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Check that the left boundary has not passed the right boundary
        # before moving from the bottom to top along the left boundary
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

print("\n")
matrix = [
          [ 0,  1,  2,  3,  4],
          [ 5,  6,  7,  8,  9],
          [10, 11, 12, 13, 14],
          [15, 16, 17, 18, 19]        
          ]

print(f"Sprial Traversal of the given matrix is: {spiral_matrix(matrix)}")
