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


def print_board(board, reveal=False, shot_positions=set()):
    """
    Print the current state of the game board.
    """
    print("   A  B  C  D  E")
    for i in range(5):
        print(f"{i+1} ", end='')
        for j in range(5):
            if (i, j) in shot_positions:
                if board[i][j] == 'X':
                    print(" H ", end='')  # Marking hit positions
                else:
                    print(" M ", end='')  # Marking miss positions
            else:
                if not reveal and board[i][j] == 'B':
                    print(" O ", end='')  # Hiding boats during regular play
                else:
                    print(f" {board[i][j]} ", end='')
        print()


def take_shot(shot_positions):
    """
    Prompt the player for a shot.
    """
    while True:
        try:
            shot = input("Enter your shot (EXAMPLE A1 OR C3 OR B2): ").upper()
            col = ord(shot[0]) - ord('A')
            row = int(shot[1]) - 1
            if (row, col) in shot_positions:
                print("You already shot at this position. Try again.")
            elif 0 <= col <= 4 and 0 <= row <= 4:
                return row, col
            else:
                print("Please enter a valid shot within the board range.")
        except (IndexError, ValueError):
            print("Enter your shot (EXAMPLE A1 OR C3 OR B2)")


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


def main_menu():
    """
    Welcome message to players
    and how to play
    """
    print("\n\nWelcome to Battleships!\n")
    print("Here you can play a game of Battleships against computer! \n")
    print("You have 10 tries to sink the 3 boats on the playfield.\n")
    print("Every boat has a unique placement.")
    print("Add 1 letter and 1 number together and press Enter!\n")
    print("Good luck!\n")
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")


def main():
    main_menu()  # Call the main menu function at the beginning
    play = True
    while play:
        board = initialize_board()
        place_boats(board)
        tries = 10
        shot_positions = set()  # Store the shot positions
        while tries > 0:
            print_board(board, reveal=False, shot_positions=shot_positions)
            print(f"\nYou have {tries} tries left.")
            row, col = take_shot(shot_positions)
            shot_positions.add((row, col))  # Add the shot position to the set
            if board[row][col] == 'B':
                print("\nHit! You sank a boat!")
                board[row][col] = 'X'
                if all(
                    board[i][j] == 'X'
                    for i in range(5)
                    for j in range(5)
                    if board[i][j] == 'B'
                ):
                    print_board(board, reveal=True)
                    print("\nCongratulations! You sank all the boats!")
                    break
            else:
                print("\nMiss!")
            tries -= 1
        else:
            print_board(board, reveal=True)
            print("\nGame Over! You ran out of tries.")
        play = play_again()


if __name__ == "__main__":
    main()
