# Noughts and Crosses aka Tic Tac Toe
Live website [here](https://noughts-and-crosses-ag.herokuapp.com/).
![heroku](img/heroku_start1.png)
![heroku](img/heroku_start.png)

# Introduction

Welcome to the famous game of Noughts and Crosses aka Tic Tac Toe for US users.
This game is played between a player (HUMAN) and the computer (BOT). 
This game is played by entering X and O in one of the nine positions.  There are three possible outcomes for the user. Win, Loose or Tie.

To win, 3 of the same symbols have to be in the same row, or column or diagonal.
The start, the "who goes first" function determines randomly who starts the game first.

As you might know, the easiest way to win at the game is to capture the corners, hence why the BOT was programmed to check for the corners first if available then the center of the outer edges.

The BOT will try and block any potential wins for the player.

If the board gets filled and no one wins, the programm will return TIE.

The player can quit at any time if they imput 'Q'.

The board's spaces are labeled 1 to 9 starting with 1 at the top left and 9 bottom right corner.

<br><br>

# User experience

## User Expectation

The main goal of this game is to challenge the user to use their strategic abilities to win a board game.

<br>

### A new user:
A new use will understand the purpose and the rules of the game as soon as the game initiates.
The rules are displayed straight away at the beginning of the game. It explains to the user how to play the game, it displays a demonstration board with the positions and it asks the user if they want to initiate the game.

### A returning user:
A returning user will know:
- How to initiate the game
- How to quit the game
- The rules of the game


A frequent user:
A frequent user would want to know:
	- If any new graphical images have been uploaded
	- if any graphics have changed or been updated.
