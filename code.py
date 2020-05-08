# tic_tac_toe
# by brussels_sprout


def intro():
    title()
    rules()
    example()


def title():
    print("\033[1m" + "Tic Tac Toe" + "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


def rules():
    print("Rules:")
    print(" • The game is played on a 3 by 3 square grid (board).")
    print(" • One player is X and the other is O. The players take turns (X plays first) putting their marks (X or O)"
          " in empty squares.")
    print(" • The first player to get 3 of their marks in a row (horizontally, vertically, or diagonally) wins the game.")
    print(" • When all 9 squares are filled, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n")
    # source: https://www.exploratorium.edu/brain_explorer/tictactoe.html (edited)


def example():
    print("Example:")
    print("╔════════╤════════╤════════╗     The coordinates of each square are shown on the board.")
    print("║ (1, 1) │ (1, 2) │ (1, 3) ║")
    print("╟────────┼────────┼────────╢     To place your mark in a specific square, just input")
    print("║ (2, 1) │ (2, 2) │ (2, 3) ║     the square's  vertical and horizontal coordinates like this: ")
    print("╟────────┼────────┼────────╢     1, 3 (example for the top right square).")
    print("║ (3, 1) │ (3, 2) │ (3, 3) ║")
    print("╚════════╧════════╧════════╝     Have fun!")


def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]  # board in initial state
    turn = 0  # turn count


def print_board(b):  # b for board; i promise this looks better during execution ok.
    print("╔═════╤═════╤═════╗")
    print(f"║  {b[0][0]}  │  {b[0][1]}  │  {b[0][2]}  ║")
    print("╟─────┼─────┼─────╢")
    print(f"║  {b[1][0]}  │  {b[1][1]}  │  {b[1][2]}  ║")
    print("╟─────┼─────┼─────╢")
    print(f"║  {b[2][0]}  │  {b[2][1]}  │  {b[2][2]}  ║")
    print("╚═════╧═════╧═════╝")


def player_turn(t):  # t for turn; return whose turn it is
    if t % 2 == 0:
        return "X"
    else:
        return "0"
    # player X has even turn count and player O odd turn count


intro()
main()
