#Start Game

import random

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print(' ')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print(' ')


    
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le))


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        if move == 'q':
            exit()
        else:
            move = int(move)
            try:
                if move > 0 and move < 10:
                    if spaceIsFree(move):
                        run = False
                        insertLetter('X', move)
                    else:
                        print('Sorry, this space is occupied!')
                else:
                    print('Please type a number within the range!')
            except:
                print('Please type a number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move


    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

# The function will check if the input is a integer number
def check_input(user_input):

    if not isnum(user_input):
        return False

    user_input = int(user_input)

    if not bounds(user_input):
        return False

    return True



def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]



# Function will establish if the input is a number 
def isnum(user_input):

    if not user_input.isnumeric():
        print("Not a valid number")
        return False
    else:
        return True


# Function establishes if the user input falls within the range of 1 and 9
def bounds(user_input):

    if user_input > 9 or user_input < 1:
        print("This number is out of range, please enter a number between 1 and 9")
        return False
    else:
        return True


# Function checks if the slot on the board has been already taken
def not_available(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else:
        return False


def coordinates(user_input):
    #This assignemt establishes the position on the board. 
    #If the position is between 0 and 2, if divided by 3 it will always be 0
    row = int(user_input / 3)
    #Finding the remainder of / 3
    col = user_input
    if col > 2:
        col = int(col % 3)
    return(row, col)


#Takes the user input and takes the board as the parameter. it adds the coordinates it havs and check if anything is there. 
def add_to_board(coords, board, active_user):

    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "x"
    else:
        return "o"


# Function checks if the user
def iswin(USER, board):
    if check_row(USER, board):
        return True
    if check_col(USER, board):
        return True
    if check_diag(USER, board):
        return True


# Function defines if user won in a row
def check_row(USER, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != USER:
                complete_row = False
                break
        if complete_row:
            print_board(board)
            print()
            return True
    return False


# Function defines if user won in a column
def check_col(USER, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != USER:
                complete_col = False
                break
        if complete_col:
            print_board(board)
            print()
            return True


# Function defines is the user has won diagonally 
def check_diag(USER, board):
    if board[0][0] == USER and board[1][1] == USER and board[2][2] == USER:
        print_board(board)
        print()
        return True
    elif board[0][2] == USER and board[1][1] == USER and board[2][0] == USER:
        print_board(board)
        print()
        return True


# This loop establishes how many turns have taken place and runns each time until the user wins or the maximum count of runs is 9.
while TURNS < 9:
    active_user = current_user(USER)
    print("")
    print_board(board)

    user_input = input("Please enter a position 1 through 9 or enter 'Q' to exit: ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Try again")
        continue
    # Converts the position on the board as the list goes from 0 to 8
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if not_available(coords, board):
        print("Position is already taken, please try again.")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break

    TURNS += 1
    if TURNS == 9:
        print("Tie!")
    USER = not USER