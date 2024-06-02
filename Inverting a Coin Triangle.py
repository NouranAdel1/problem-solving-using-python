def flip_triangle(triangle):
    num_rows = len(triangle)
    # Create a new triangle to store the flipped state
    flipped_triangle = [[0 for _ in range(i)] for i in range(num_rows, 0, -1)]

    # Loop through each row and each coin in the original triangle
    for row in range(num_rows):
        for col in range(len(triangle[row])):
            # Calculate the new row and column for the coin after flipping
            new_row = num_rows - row - 1
            new_col = col

            # Move the coin to its new position in the flipped triangle
            flipped_triangle[new_row][new_col] = triangle[row][col]

    # Replace the original triangle with the flipped triangle
    triangle[:] = flipped_triangle[:]


def display_triangle_initial(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))  # Maximum width of the final row
    for i, row in enumerate(triangle):
        padding = ' ' * (max_width - len(row))  # Padding to align triangle
        print(padding + ' '.join(map(str, row)))

def display_triangle_final(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))  # Maximum width of the final row
    for i, row in enumerate(triangle):
        new_row = [str(item) for item in row]  # Convert integers to strings for proper length calculation
        padding = ' ' * (num_rows - len(new_row))  # Padding to align triangle
        print(padding + ' '.join(new_row))


def create_triangle(num_rows):
    triangle = []
    for i in range(1, num_rows + 1):
        triangle.append([0] * i)
    return triangle


# Prompt user to enter the number of rows in the coin triangle
num_rows = int(input("Enter the number of rows in the coin triangle: "))

# Create the initial state of the coin triangle
initial_triangle = create_triangle(num_rows)
print("Initial state of the coin triangle:")
display_triangle_initial(initial_triangle)

# Flip the triangle
flip_triangle(initial_triangle)

# Display the final state of the coin triangle
print("\nFinal state of the coin triangle after flipping:")
display_triangle_final(initial_triangle)
