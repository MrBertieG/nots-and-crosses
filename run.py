#Start Game

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
            print(f"{slot} ", end="")
        print()


#This is the Quit function where the user can exit by pressing 'q'
def quit(user_input):

    if user_input.lower() == "q":
        print('Thanks for playing')
        return True
    else:
        return False

#The function will check if the input is a integer number
def check_input(user_input):

    if not isnum(user_input): 
        return False

    user_input = int(user_input)

    if not bounds(user_input): 
        return False

    return True

#Function will establish if the input is a number 
def isnum(user_input):

    if not user_input.isnumeric():
        print("Not a valid number")
        return False
    else: 
        return True

#Function establishes if the user input falls within the range of 1 and 9
def bounds(user_input):

    if user_input > 9 or user_input < 1:
        print("This number is out of range, please enter a number between 1 and 9")
        return False
    else: 
        return True


def not_available(coords):

def coordinates():
    #This assignemt establishes the position on the board. 
    #If the position is between 0 and 2, if divided by 3 it will always be 0
    row = int(user_input / 3)
    #Finding the remainder of / 3
    col = user_input
    if col > 2: col = int(col % 3)
    return(row, col)


while True:
    print_board(board)
    user_input = input("Please enter a position 1 through 9 or enter 'q' to quit:")
    if quit(user_input): 
        break
    if not check_input(user_input):
        print("Try again")
        continue
    #Converts the position on the board as the list goes from 0 to 8
    user_input = int(user_input) - 1
    coords = coordinates(user_input)