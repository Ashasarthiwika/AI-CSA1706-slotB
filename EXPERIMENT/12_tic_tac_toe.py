board = [" "] * 9

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in winning
    )


player = "X"

for turn in range(9):
    display()

    position = int(input("Enter position (1-9): ")) - 1

    if board[position] != " ":
        print("Position already occupied!")
        continue

    board[position] = player

    if check_winner(player):
        display()
        print("Player", player, "wins!")
        break

    player = "O" if player == "X" else "X"
else:
    display()
    print("Game Draw!")
