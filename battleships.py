import random
from flask import Flask, render_template, request

app = Flask(__name__)

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
    board_str = "   A  B  C  D  E\n"
    for i in range(5):
        board_str += f"{i+1} "
        for j in range(5):
            if not reveal and board[i][j] == 'B':
                board_str += " O "
            else:
                board_str += f" {board[i][j]} "
        board_str += '\n'
    return board_str

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    play = True
    while play:
        board = initialize_board()
        place_boats(board)
        tries = 6
        while tries > 0:
            board_str = print_board(board)
            board_str += f"\nYou have {tries} tries left.\n"
            # Take input from the web form instead of the console
            #row, col = take_shot()
            # Instead of taking input from console, get input from the form
            row = int(request.form['row']) - 1
            col = int(request.form['col']) - 1

            if board[row][col] == 'B':
                board_str += "\nHit! You sank a boat!"
                board[row][col] = 'X'
                if all(board[i][j] == 'X' for i in range(5) for j in range(5) if board[i][j] == 'B'):
                    board_str += print_board(board, reveal=True)
                    board_str += "\nCongratulations! You sank all the boats!"
                    break
            else:
                board_str += "\nMiss!"
            tries -= 1
        else:
            board_str += print_board(board, reveal=True)
            board_str += "\nGame Over! You ran out of tries."
        play = play_again()
    return render_template('play.html', board=board_str)

if __name__ == "__main__":
    app.run(debug=True)
