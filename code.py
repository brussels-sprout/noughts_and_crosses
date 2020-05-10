# noughts_and_crosses
# by brussels_sprout


def intro():
    title()
    rules()
    example()


def title():
    print("\033[1m" + "Noughts and Crosses" + "\033[0;0m" + "\nby brussels-sprout\n")
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
    print("║ (1, 1) │ (1, 2) │ (1, 3) ║     To place your mark in a specific square, just input")
    print("╟────────┼────────┼────────╢     the square's  vertical and horizontal coordinates like this:")
    print("║ (2, 1) │ (2, 2) │ (2, 3) ║     1, 3 (example for the top right square).")
    print("╟────────┼────────┼────────╢     Note that you cannot overwrite an already set mark.")
    print("║ (3, 1) │ (3, 2) │ (3, 3) ║")
    print("╚════════╧════════╧════════╝     Have fun!")


def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]  # board in initial state
    turn = 0  # turn count
    cont = True  # cont for continue

    print("\n-----Play-----\n")

    def play():
        nonlocal board
        nonlocal turn
        nonlocal cont

        while cont:
            if turn <= 8:  # at 9th turn (turn == 8) board is full
                player = player_turn(turn)
                print_board(board)

                coords = input(f"{player}'s turn: ")
                print()
                if check_input(coords):
                    coords = adjust_input(coords)

                    v_coord = int(coords[0]) - 1  # v for vertical; - 1 adjust for index starting at 0
                    h_coord = int(coords[1]) - 1  # h for horizontal; - 1 adjust for index starting at 0

                    if not check_overwrite(board, v_coord, h_coord):
                        board[v_coord][h_coord] = player
                        if check_win(board):
                            print_board(board)
                            print(f"\nPlayer {player} won!")

                            cont = False
                        turn += 1
                    else:
                        print("The input is invalid; look at the example above for valid input format. Try again.\n")
                        play()
                else:
                    print("The input is invalid; look at the example above for valid input format. Try again.\n")
                    play()
            else:
                cont = False
                print("Tie!")

    play()

    print("\n-----Game over-----\n")

    end()


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


def check_input(coords):
    coords = coords.replace(" ", "")  # coords for coordinates
    if len(coords) == 3:
        if coords[1] == ",":
            if (coords[0] + coords[2]).isdigit():
                if 1 <= int(coords[0]) <= 3 and 1 <= int(coords[2]) <= 3:
                    return True
    return False


def adjust_input(coords):  # only works after check_input(coords) is True
    return coords.replace(" ", "").replace(",", "")


def check_overwrite(board, v_coord, h_coord):  # checks if current coordinates input will overwrite previous one
    return board[v_coord][h_coord] != " "


def check_win(b):  # b for board
    for v in range(3):  # check for horizontal line
        if b[v][0] == b[v][1] == b[v][2] != " ":
            return True

    for h in range(3):  # check for vertical line
        if b[0][h] == b[1][h] == b[2][h] != " ":
            return True

    if b[0][0] == b[1][1] == b[2][2] != " ":  # check for top left to bottom right diagonal line
        return True

    if b[0][2] == b[1][1] == b[2][0] != " ":  # check for top right to bottom left diagonal line
        return True

    return False


def end():
    if input("Input any character(s) to play again or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        main()


intro()
main()
