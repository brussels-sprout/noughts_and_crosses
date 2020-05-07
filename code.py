# tic_tac_toe
# by brussels_sprout


def title():
    print("\033[1m" + "Tic Tac Toe" + "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


def rules():
    print("RULES:")
    print(" • The game is played on a 3 by 3 square grid (board).")
    print(" • One player is X and the other is O. The players take turns putting their marks (X or O) in empty squares.")
    print(" • The first player to get 3 of their marks in a row (horizontally, vertically, or diagonally) wins the game.")
    print(" • When all 9 squares are filled, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    print(" • Note: squares filled with # are empty.\n")
    # source: https://www.exploratorium.edu/brain_explorer/tictactoe.html (edited)


def main():
    board = [
        ["#", "#", "#"],
        ["#", "#", "#"],
        ["#", "#", "#"]
    ]
    print_board(board)


def print_board(b):  # b for board
    print("╔═══╤═══╤═══╗")
    print(f"║ {b[0][0]} │ {b[0][1]} │ {b[0][2]} ║")
    print("╟ ─ ┼ ─ ┼ ─ ╢")
    print(f"║ {b[1][0]} │ {b[1][1]} │ {b[1][2]} ║")
    print("╟ ─ ┼ ─ ┼ ─ ╢")
    print(f"║ {b[2][0]} │ {b[2][1]} │ {b[2][2]} ║")
    print("╚═══╧═══╧═══╝")


title()
rules()
main()
