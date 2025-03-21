import math

# Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check the winner
def check_winner():
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Check if moves are left
def is_moves_left():
    return any(' ' in row for row in board)

# Minimax algorithm with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):
    winner = check_winner()
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif not is_moves_left():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

# AI makes the best move
def best_move():
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = 'O'

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()
    
    while True:
        if not is_moves_left() or check_winner():
            break
        
        # Player's turn
        try:
            row, col = map(int, input("Enter your move (row and column: 0, 1, or 2): ").split())
            if board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
            board[row][col] = 'X'
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")
            continue
        
        print_board()
        
        if check_winner() or not is_moves_left():
            break
        
        print("AI is making its move...")
        best_move()
        print_board()

    winner = check_winner()
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
