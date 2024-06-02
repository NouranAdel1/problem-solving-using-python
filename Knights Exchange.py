
from collections import deque

# Possible knight moves
knight_moves = [(2, 1), (1, 2), (-2, -1), (-1, -2), (2, -1), (-2, 1), (1, -2), (-1, 2)]

# Check if the position is inside the board and not occupied
def is_valid_move(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 0

# Print board state
def print_board(board):
    for row in board:
        print(' '.join([str(cell) for cell in row]))
    print()

# BFS to find the minimum number of moves to exchange knights
def exchange_knights(start_board):
    rows = len(start_board)
    cols = len(start_board[0])

    # Convert board state to tuple to use it as a dictionary key
    start_state = tuple(tuple(row) for row in start_board)

    queue = deque([(start_state, 0)])  # Queue for BFS: (board_state, num_moves)
    visited = set([start_state])  # Set of visited states

    while queue:
        current_state, num_moves = queue.popleft()

        # Convert current state to list for easier manipulation
        current_board = [list(row) for row in current_state]

        # Check if we reached the desired end board state
        if current_board == [[1, 1, 1], [0, 0, 0], [0, 0, 0], [-1, -1, -1]]:
            end_board = current_board
            return num_moves, end_board

        # Explore all possible knight moves from this state
        for i in range(rows):
            for j in range(cols):
                knight = current_board[i][j]
                if knight != 0:
                    for move_x, move_y in knight_moves:
                        new_x = i + move_x
                        new_y = j + move_y

                        if is_valid_move(current_board, new_x, new_y):
                            next_board = [row[:] for row in current_board]
                            next_board[new_x][new_y] = knight
                            next_board[i][j] = 0  # Set the old position to 0
                            next_state = tuple(tuple(row) for row in next_board)

                            if next_state not in visited:
                                visited.add(next_state)
                                queue.append((next_state, num_moves + 1))  # Increment move count

# Example start_board (4x3)
start_board = [
    [-1, -1, -1],
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1]
]

# Call the function to get the minimum number of moves and the end board
min_moves, end_board = exchange_knights(start_board)

# Print the start board
print("Start Board:")
print_board(start_board)

# Print the end board
print("End Board:")
print_board(end_board)

print("Minimum number of moves to exchange knights:", min_moves)
