# Noughts and Crosses aka Tic Tac Toe
Live website [here](https://noughts-and-crosses-ag.herokuapp.com/).
![heroku](img/heroku_start1.png)
![heroku](img/heroku_start.png)

# Introduction

Welcome to the famous game of Noughts and Crosses aka Tic Tac Toe for US users.
This game is played between a player (HUMAN) and the computer (BOT). 
This game is played by entering X and O in one of the nine positions.  There are three possible outcomes for the user. Win, Loose or Tie.

The board has spaces labeled from 1 to 9 starting with 1 at the top left and 9 bottom right corner.

To win, a player has to enter 3 of the same symbols in the same row, or column or diagonal. Whoever does that first wins.

The start of this program is determined by the "who goes first" function, meaning that the function chooses randomly a number between 0 and 1. The 0 is allocated to the Player(HUMAN) and the 1 to the Computer(BOT).

As you might know, the easiest way to win at the game is to capture the corners, hence why the BOT was programmed to check for the corners first for availability, then the center and lastly the center of the outer edges.

The BOT will try and block any potential wins for the player.

If the board gets filled and no one wins, the programm will assume it's a TIE.

The player can quit at any time if they imput 'Q'.

<br><br>

## <a name="top">Table of Contents</a>

### [1. User Experience](#user-ex) 

- Design Approach
- User Expectations
	- New Users
	- Returning Users
	- Frequent Users
- Color Design
### [2. Features](#features)
- Interractive Gameplay
- Input Validation
- Code Features

### [3. Wireframe](#wireframe)
### [4. Deployment](#deployment)
### [5. Manual Testing](#manual-testing)
### [6. Technologies Used](#tech-used)
### [7. Bugs](#bugs)
### [8. Credits](#credits)

<br><br>


[Top of the page](#top)
# <a name="user-ex">1. User Experience</a>

## Design Approach 

The UX design was developed with the idea of keeping everything simple and straight forward but with some added featuers such as the colour scheam and ASCII messages.

Originally the program was designed to be played between two real users, however I have soon realized that this was a bit too simple and not as entertaining as if a computer "AI" element was introduced. I found that this has made the UX a lot more enjoyable. 
<br><br>

## User Expectation

The main goal of this game is to challenge the user to use their strategic abilities to win a board game. The game will need to be clear from the begining.

<br>

- ### A new user:
	A new use will understand the purpose and the rules of the game as soon as the game initiates.
	The rules are displayed straight away at the beginning of the game. It explains to the user how to play the game, it displays a demonstration board with the positions and it asks the user if they want to initiate the game.

<br>

- ### A returning user:
	A returning user will know how to :
	- initiate the game
	- quit the game
	- play the game

<br>

- ### A frequent user:
	A frequent user would want to know:
	- If any new graphical images have been uploaded
	- if any graphics have changed or been updated.

<br>

## Color Design

Since this program is designed to challenge and entertain, I have decided to add the Gold colour in as it contrasts with the black background and makes the text more vibrant.

The red colour is used to underline a problem with the user's inputs and also to indicate that the player has lost. Since the ASCII Art for "YOU LOOSE" is meant to replicate running 'blood' I have also chosen the red colour for it as it would add drama. <br>
![loose text](img/you_loose_play_txt.png)

<br><br>

# 2. Features
## Interractive Gameplay
The user will play against a computer. The computer will choose different positions on the board depending on the user's previous input. The moves are not always the same.

## Input Validation
The user has a choice of various inputs. If the user enters a string or number not within the range then the following message will appear, prompting the user to try again.

- "Initiate the game? (Y/N):" <br>
	![start validation](img/validation_start.png)

- "Place your 'X' HUMAN (position 1 - 9) or press 'Q' to give up :"<br>
	![play validation](img/validation_play.png)

## Game Colour Features & ASCII Art
The game has different colour features and additional ASCII Art for a better contrast and visual appeal.

- Game Intro
	![text intro](img/heroku_start1.png)

- "You WON"
	![winning](img/you_won_play.png)

- "Bot is the winner"
	![loosing](img/you_loose_play.png)

- "The game is a tie"
	![tie](img/tie_play.png)

<br>

## Code Features

- The "flip a coin start" is a small code which allows the program to decide who goes first. It's a very simple piece of code, but it playes a big part in the running of the program and UX.
![random start player](img/ran_start_player.png)
![random start computer](img/ran_start_comp.png)

- The Computer will block a possible winning move.<br>
	![blocking a move](img/block_move.png)<br>
in this code the program makes a copy of the board and uses the player's inputs to see if it can win on the next move. If yes, then it will enter the symbol in the possible winning position.


## <a name="wireframe">3. Wireframe</a>
The wireframe was created using Lucidchart.

![wireframe](img/wireframe_xando.jpeg)