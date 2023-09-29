# NumberGuessingAI

Welcome to NumberGuessingAI! In this game, you think of a number between 1 and 1000, and the computer will try to guess it. What's the twist? The computer will guess your number in 10 moves or fewer, provided you don't cheat!

## How to Play

1. **Setup:** Clone this repository and navigate to the root directory.
2. **Starting the Game:** Execute `python number_guessing_ai.py` (or the relevant filename).
3. **Gameplay:** 
   - Think of a number between 1-1000.
   - The computer will make a guess. Respond with:
     - "Too small" if the computer's guess is too low.
     - "Too big" if the computer's guess is too high.
     - "You win" if the computer correctly guesses your number.

## Features

- **Smart Guessing:** The computer employs a binary search algorithm, ensuring it guesses the correct number in no more than 10 moves.
- **Interactive Gameplay:** Play your role honestly and watch as the computer narrows down the correct number!
  
## Future Improvements

- [ ] Adding a game history feature to review past games.
- [ ] Implement a scoring system to rate user honesty.

## Author

RafalCzerwik

## License

This project is open source. Users are free to modify and distribute the code. Please refer to the attached LICENSE file for detailed terms and conditions.

## Feedback & Contributions

Feedback is always welcome! If you find any issues or would like to suggest improvements, please raise an issue. Contributions are also appreciated. Simply fork this repository, make your changes, and submit a pull request.

Enjoy the game and see if you can outsmart the computer!
