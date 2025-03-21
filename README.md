# Number Guessing Game

## Description
The **Number Guessing Game** is a fun and interactive Python program where players can either guess a randomly generated number or have the computer guess a number they have in mind. This game provides two modes of play:

1. **User Guesses the Number**: The computer randomly selects a number, and the player tries to guess it with hints.
2. **Computer Guesses the Number**: The player thinks of a number, and the computer attempts to guess it using binary search logic.

## Features
- Player guesses a random number generated by the computer.
- The computer intelligently guesses a number chosen by the player.
- Interactive hints help refine the guesses.
- Fun and engaging way to practice logic and number prediction.

## How to Run
### Prerequisites
- Python 3.x installed on your system.

### Steps to Run
1. Download or clone the repository.
2. Open a terminal or command prompt in the project directory.
3. Run the script using the command:
   ```bash
   python number_guessing_game.py
   ```

## Game Rules
### User Guesses the Number:
- The computer selects a random number between **1 and X**.
- The user inputs their guess.
- The game provides feedback:
  - "Too high" if the guess is greater than the number.
  - "Too low" if the guess is smaller than the number.
  - "Correct" if the guess matches the number.
- The game continues until the user guesses correctly.

### Computer Guesses the Number:
- The user thinks of a number between **1 and X**.
- The computer makes a guess and asks the user for feedback:
  - "H" (High) if the guess is too high.
  - "L" (Low) if the guess is too low.
  - "C" (Correct) if the guess is right.
- The computer adjusts its guesses accordingly until it finds the correct number.

## Example Output
```
✨✨ Welcome to Number Guessing Game ✨✨
Guess a number between 1 and 10: 5
😞 Sorry, guess again. Number 5 is too low.
Guess a number between 1 and 10: 7
🎊 Congratulations, You Won the Game by choosing Number 7 correctly. 🎉
```
```
If 50 too high (H), too low (L), or Correct (C)?? L
If 75 too high (H), too low (L), or Correct (C)?? H
🥳 Congratulations, Computer guessed the correct number. It's Number 62 ✨
```

## Technologies Used
- Python
- Random Library (for generating random numbers)

## Future Enhancements
- Add difficulty levels.
- Implement a graphical user interface (GUI).
- Keep track of the number of attempts.

## Author
- Developed by [Syeda Rajda Bano]

Enjoy the game! 🎮✨

