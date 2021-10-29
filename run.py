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
        print('Thanks for playing')
        return True

def check_input(user_input):
    # check if its a number
    if not isnum(user_input): return False
    user_input = int(user_input)
    # check if it's 1 - 9
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("Not a valid number")
        return False
    else: return True

def bounds(user_input):


while True:
    user_input = input("Please enter a position 1 through 9 or enter 'q' to quit:")
    if quit(user_input): break
    if not check_input(user_input):
        print("Try again")
        continue