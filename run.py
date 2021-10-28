#tic tac toe start

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(board):
    """
    Prints the slots vertically to the terminal
    """
    for row in board:
        for slot in row:
            print(f"{slot}", end="")
        print()

print_board(board)

def quit(user_input):
    if user_input.lower() == "q":
        return True

"""
while True:
    user_input = input("Please enter a position 1 through 9 or enter 'q' to quit:")
    if quit(user_input) = True:
        break
"""