def is_valid_move(board, start, end):
    if start < 0 or start >= len(board) or end < 0 or end >= len(board):
        return False  #checks if start and end are in array boundries 
    if board[start] == 1 and board[end] == 0 and board[(start + end) // 2] == 1:
        return True    #checks if start=1 and end=0 & they have 1 between them
    return False

def make_move(board, start, end):  #moves peg from start position to end position, puts 0 in start position and at position where the peg that was jumped over
    board[start] = 0
    board[(start + end) // 2] = 0
    board[end] = 1

def count_pegs(board):  #Counts the number of pegs
    return sum(board)

def find_solution(board):
    n = len(board)
    if count_pegs(board) == 1: #if remaining pegs=1 . solutions exists, return true 
        return True
    for i in range(n):
        if board[i] == 1:
            if is_valid_move(board, i, i+2):
                make_move(board, i, i+2)
                if find_solution(board):
                    return True
                make_move(board, i+2, i)
            if is_valid_move(board, i, i-2):
                make_move(board, i, i-2)
                if find_solution(board):
                    return True
                make_move(board, i-2, i)
    return False

def solve_peg_solitaire(n, initial_board):
    if n % 2 != 0 or n <= 2:
        print("Invalid input, n should be even and greater than 2.")
        return
    if len(initial_board) != n:
        print("Initial board size does not match n.")
        return
    if sum(initial_board) != n - 1:
        print("Invalid initial board configuration.")
        return
    if find_solution(initial_board):
        print("Valid solution exists:")
        print(initial_board)
    else:
        print("No valid solution exists.")


n = int(input("Enter the size of the board (even number greater than 2): "))
initial_board = list(map(int, input("Enter the initial board configuration (0 for empty, 1 for pegs): ").split()))
solve_peg_solitaire(n, initial_board)

