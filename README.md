# Snake Game In Python

---

![screenshot](https://github.com/AadiGodzilla/Snake-Game-Python/blob/main/assets/screenshot.png?raw=true)

## Introduction

This is my rendition of the popular Snake arcade game
written in python with the support of the [pygame](https://www.pygame.org/news) 2D game library

## Gameplay

- In this game, we control a hungry snake which eats apples.
- These apples appear in a reappear on a random position on the screen once the snake has eaten the apple.
- Each time the snake eats the apple, it contributes to the score and the length of the snake to be incremented.

## Controls

- ```W``` or ```UP ARROW```: Move snake up
- ```S``` or ```DOWN ARROW```: Move snake down
- ```A``` or ```LEFT ARROW```: Move snake left
- ```D``` or ```RIGHT ARROW```: Move snake right
- ```ESCAPE```: Pause / Resume the Game

## Game Over Conditions

The game will come to an end when either of the following conditions is met:

- When the head of the snake collides to a segment of its body
- When the head of the snake goes out of bounds of the window

Once the game is over, The player can ```press any key``` to resume the game which will reset the size and position of the snake to that at the beginning of the game
aswell as set the score to zero 
## Building the Game 

The steps of building the game from this GitHub repository

### Prerequisites:
- Ensure ```git``` be installed
- Python Package Manager ```pip``` be installed
- Ensure that your have ```python``` version greater than ```3.11```

### Steps to Build:

- Clone this repository using the ```git clone``` command or run the following commands in the terminal \
```git clone https://github.com/AadiGodzilla/Snake-Game-Python``` \
```cd Snake-Game-Python```
- Run the following command to install the required packages in the ```requirements.txt``` file: \
```pip install -r requirements.txt```
- At last, run the game file using ```python src/main.py```
