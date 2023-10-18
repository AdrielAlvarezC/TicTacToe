import random

# Function to initialize the game board
def initialize_board():
    return [' ' for _ in range(9)]

# Function to check if a player has won
def check_win(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

# Function for an AI move
def ai_move(board, player):
    possible_moves = [i for i, spot in enumerate(board) if spot == ' ']
    move = random.choice(possible_moves)  # AI picks a random valid spot
    board[move] = player

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to print the board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

# Main function to run the game
def main():
    current_board = initialize_board()
    current_player = 'X'  # Start with player X

    while True:
        print_board(current_board)
        ai_move(current_board, current_player)
        winner = check_win(current_board)
        if winner:
            print_board(current_board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(current_board):
            print_board(current_board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'  # Switch player

if __name__ == "__main__":
    main()
