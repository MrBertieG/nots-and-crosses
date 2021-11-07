# Nouts and Crosses Game
# The gamne is played between a Player(HUMAN) and the Computer(BOT)
# The start of the game is established randomly
# The computer will always check if any of the corners are free. As you might know, the easiest way to win at the game is to capture the corners.
# The computer will randomly select the corners or thew center if no corners are free
# The computer will try and block any potential wins for the player
# If the board gets filled and no one wins, the programm will return TIE.
# The player can quit at any time if they imput 'Q'
# The board's spaces are labeled 1 to 9 starting with 1 at the top left and 9 bottom right corner

import random

# Creates a board with 10 empty values
board = [' ' for x in range(10)]


# Demonstration Board displayes as an intro
def demoBoard():
    print(' ')
    print('   |   | ')
    print(' 1 | 2 | 3')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' 4 | 5 | 6')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' 7 | 8 | 9')
    print('   |   |')
    print(' ')


# This allows to insert any letters in any given position
def insertLetter(letter, pos):
    board[pos] = letter


# Checks if the space is availabe to use. If not equal to empty it will return False
def spaceIsFree(pos):
    return board[pos] == ' '


# Main board printed each time a player enters a letter. The board contains spaces from 1 to 9, with no 0
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


# Establishes the winning combimnations on the board. It akes the two parameters bo(board) and le(letter)
# and it will go through each combinatiomn
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le))


# Thie player's move input. If the player's choce is within the parameters 1 - 9 & the space is available
# it will insert it on the board.
# If the player inoputs 'Q' the game will terminate
def playerMove():
    run = True
    while run:
        move = input('Place your \'X\' HUMAN (1-9) or press \'Q\' to give up : ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Place is taken HUMAN')
            else:
                print('Numbers 1 - 9 only')
        except:
            if move == 'q':
                quit()
            else:
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
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move


def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


gamePlay = True


def main():
    if random.randint(0, 1) == 0:
        while not(isBoardFull(board)):
            if not(isWinner(board, 'O')):
                playerMove()
                printBoard(board)
            else:
                print('BOT is the winner, you LOOSE!')
                break

            if not(isWinner(board, 'X')):
                move = compMove()
                if move == 0:
                    print('Tie Game!')
                else:
                    insertLetter('O', move)
                    print('BOT placed an \'O\' in position', move , ':')
                    printBoard(board)
            else:
                print('You win HUMAN!')
                break

    else:
        while not(isBoardFull(board)):
            if not(isWinner(board, 'X')):
                move = compMove()
                if move == 0:
                    print('Tie Game!')
                    break
                else:
                    insertLetter('O', move)
                    print('BOT placed an \'O\' in position', move , ':')
                    printBoard(board)
            else:
                print('You win HUMAN!')
                break

            if not(isWinner(board, 'O')):
                if isBoardFull(board):
                    print('Tie Game!')
                    break
                else:
                    playerMove()
                    printBoard(board)
            else:
                print('BOT is the winner, you LOOSE!')
                break



print('')
print('BOT: Welcome HUMAN, do you dare to challenge me to a deadly game of Noughts and Crosses aka Tic Tac Toe?')
print('')
print('BOT: We will let the universe decide who starts, brace yourself HUMAN!')
print('')
begin = input('Start the game? (Y/N): ')
demoBoard()


while gamePlay:
    if begin.lower() == 'y':
        main()
    elif begin.lower() == 'n':
        print('Goodbye. GAME OVER')
        print('')
        quit()
    else:
        print(' Please enter Y or N')

    answer = input('Do you want to play again? (Y/N): ')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        print('')
        main()
    else:
        break