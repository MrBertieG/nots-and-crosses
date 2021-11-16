import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Creates a board with 10 empty values
board = [' ' for x in range(10)]


# Demonstration Board displayiong position layout
demo_board = """
   |   |
 1 | 2 | 3
   |   |
-----------
   |   |
 4 | 5 | 6
   |   |
-----------
   |   |
 7 | 8 | 9
   |   |
"""

lose_message = """
▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░
 ░ ░
"""

won_message = """

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝
   """

game_over = """

 ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████
██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██
██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████
██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██
 ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██
"""

tie_game = """
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
     ▐░▌          ▐░▌     ▐░▌
     ▐░▌          ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄
     ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌
     ▐░▌          ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀
     ▐░▌          ▐░▌     ▐░▌
     ▐░▌      ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀
"""


def insert_letter(letter, pos):
    """
    Method allows to insert any letters into any given
    positions.
    """
    board[pos] = letter


def space_is_free(pos):
    """
    Checks if the space is availabe to use.
    If not equal to empty it will return False
    """
    return board[pos] == ' '


def print_board(board):
    """
    Main board is printed each time a player enters a letter.
    The board contains spaces from 1 to 9, with no 0
    """
    print(' ')
    print(Fore.YELLOW + '   |   |')
    print(Fore.YELLOW + ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(Fore.YELLOW + '   |   |')
    print(Fore.YELLOW + '-----------')
    print(Fore.YELLOW + '   |   |')
    print(Fore.YELLOW + ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(Fore.YELLOW + '   |   |')
    print(Fore.YELLOW + '-----------')
    print(Fore.YELLOW + '   |   |')
    print(Fore.YELLOW + ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(Fore.YELLOW + '   |   |')
    print(' ')


def is_winner(board, letter):
    """
    Establishes the winning combimnations on the board.
    It makes the two parameters board and letterand
    it will go through each combinatiomn.
    """
    if (board[7] == letter and board[8] == letter and board[9] == letter):
        return True
    elif (board[4] == letter and board[5] == letter and board[6] == letter):
        return True
    elif (board[1] == letter and board[2] == letter and board[3] == letter):
        return True
    elif (board[1] == letter and board[4] == letter and board[7] == letter):
        return True
    elif (board[2] == letter and board[5] == letter and board[8] == letter):
        return True
    elif (board[3] == letter and board[6] == letter and board[9] == letter):
        return True
    elif (board[1] == letter and board[5] == letter and board[9] == letter):
        return True
    elif (board[3] == letter and board[5] == letter and board[7] == letter):
        return True


def player_move():
    """
    This is the player's move input. If the player's choice is within
    the parameters 1 to 9 & the space is available it will insert it
    on the board. If the player inoputs 'Q' the game will terminate.
    """
    run = True
    while run:
        move = input(
            'Place your \'X\' HUMAN (position 1 - 9)'
            'or press \'Q\' to give up : ')
        try:
            move = int(move)
            # If the position is between the parameters the code will continue
            if move > 0 and move < 10:
                # Checks to see if the position sellected is avalable
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print(Fore.RED + 'Place is taken HUMAN')
            else:
                # User input validation
                print(Fore.RED + 'Numbers 1 - 9 only')
        except:
            # Pressing Q will terminate the game
            if move == 'q':
                print(game_over)
                quit()
            else:
                print(Fore.RED + 'Please type a number!')


def comp_move():
    """
    This is the 'AI' function, where it checks for possible free corners.
    The for loop will iterate over the board parameter, appending a copy
    of the string values in the original board to the duplicate board.
    """
    # Creates a list of possible winning moves
    possible_moves = [x for x, letter in enumerate(board)
                      if letter == ' ' and x != 0]
    move = 0
    # Checks for possible winning moves and attempts to block it
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    # Checks to see if the corners are open
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    # If one or more corners are open then it will randomly select one
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    # This is the center of the board,
    # another advantage in the game
    if 5 in possible_moves:
        move = 5
        return move

    # Looks for the middle of the 4 edges
    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    # If any edges are open it will randomly select one
    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


def select_random(li):
    """
    Random Function will select a position randomly,
    based on the availability.
    """
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def is_board_full(board):
    """
    Check to see if the board has one or more spaces taken.
    If so it will return False.
    """
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    """
    This is the main body of the functioning game.
    """
    # This will randomly choose if the player or computer will start first
    if random.randint(0, 1) == 0:
        # This is the 'Player starts first' option.
        # If the board is full it will terminate
        while not(is_board_full(board)):
            # If the game hasn't been won it will continue
            if not(is_winner(board, 'O')):
                print('')
                player_move()
                print_board(board)
            else:
                print(Fore.RED + 'BOT is the winner')
                print(Fore.RED + lose_message)
                break

            if not(is_winner(board, 'X')):
                move = comp_move()
                if move == 0:
                    print('The game is a Tie')
                    print(tie_game)
                else:
                    insert_letter('O', move)
                    print('BOT placed an \'O\' in position', move, ':')
                    print_board(board)
            else:
                print(Fore.GOLD + 'You win HUMAN!')
                print(Fore.YELLOW + won_message)
                break

    else:
        # This is the 'Computer starts first' option
        # If the board is full it will terminate
        while not(is_board_full(board)):
            if not(is_winner(board, 'X')):
                move = comp_move()
                if move == 0:
                    print('The game is a Tie')
                    print(tie_game)
                    break
                else:
                    insert_letter('O', move)
                    print('BOT placed an \'O\' in position', move, ':')
                    print_board(board)
            else:
                print(Fore.GOLD + 'You win HUMAN!')
                print(Fore.YELLOW + won_message)
                break

            if not(is_winner(board, 'O')):
                if is_board_full(board):
                    print('The game is a Tie')
                    print(tie_game)
                    break
                else:
                    player_move()
                    print_board(board)
            else:
                print('BOT is the winner')
                print(Fore.RED + lose_message)
                break


introduction_message = """
___   ___    ____    ____   _______.     ______
\  \ /  /    \   \  /   /  /       |    /  __  \'
 \  V  /      \   \/   /  |   (----`   |  |  |  |
  >   <        \      /    \   \       |  |  |  |
 /  .  \        \    / .----)   |      |  `--'  |
/__/ \__\        \__/  |_______/        \______/


BOT: Welcome HUMAN, do you dare to challenge me to a deadly
game of Noughts and Crosses aka Tic Tac Toe?

We will battle with X and O. Whoever can get 3 in a row,
a column or in a diagonal Wins!

The numbered positions on the board indicate the spaces
you need to occupy. Use your keyboard to enter a number
from 1 to 9.

BOT: We will let the universe decide who starts first,
brace yourself HUMAN!

"""
print(Fore.YELLOW + introduction_message)
print(Fore.YELLOW + demo_board)


# The while loop allows th game to run.
while True:

    while True:
        begin = input('Initiate the game? (Y/N): ')
        if begin.lower() == 'y':
            main()
            break

        elif begin.lower() == 'n':
            print(Fore.RED + game_over)
            print('')
            quit()
        else:
            print('Select Y or N')

    while True:
        answer = input('Do you want to play again? (Y/N): ')
        print(Fore.YELLOW + demo_board)
        if answer.lower() == 'y' or answer.lower == 'yes':
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            print('')
            main()

        elif answer.lower() == 'n':
            print(Fore.RED + game_over)
            print('')
            quit()

        else:
            print('Select Y or N')
