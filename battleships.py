import random

def initialize_board():
    """
    Initialize the game board with empty cells.
    """
    return [['O' for _ in range(5)] for _ in range(5)]

def place_boats(board):
    """
    Randomly place 3 boats on the board.
    """
    boat_positions = []
    for _ in range(3):
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if (row, col) not in boat_positions:
                boat_positions.append((row, col))
                board[row][col] = 'B'
                break

def print_board(board, reveal=False):
    """
    Print the current state of the game board.
    """
    print("   A  B  C  D  E")
    for i in range(5):
        print(f"{i+1} ", end='')
        for j in range(5):
            if not reveal and board[i][j] == 'B':
                print(" O ", end='')
            else:
                print(f" {board[i][j]} ", end='')
        print()

def take_shot():
    """
    Prompt the player for a shot.
    """
    while True:
        try:
            shot = input("Enter your shot (e.g., A3): ").upper()
            col = ord(shot[0]) - ord('A')
            row = int(shot[1]) - 1
            if 0 <= col <= 4 and 0 <= row <= 4:
                return row, col
            else:
                print("Please enter a valid shot within the board range.")
        except (IndexError, ValueError):
            print("Please enter a valid shot (e.g., A3).")

def play_again():
    """
    Prompt the player if they want to play again.
    """
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ('yes', 'no'):
            return choice == 'yes'
        else:
            print("Please enter 'yes' or 'no'.")