def guess_number():
    """
    This function allows the computer to guess a number that the user has thought of
    between 1 and 1000. The user provides feedback to the computer to help it guess the
    correct number. The computer will try to guess the number in 10 attempts or less.
    """
    min_val = 1
    max_val = 1000
    attempts = 0

    print("Think of a number between 1 and 1000, and I'll guess it in 10 attempts or less!")

    while attempts < 10:
        guess = int((max_val - min_val) // 2) + min_val
        print(f"I'm guessing: {guess}")
        response = input("Enter your response (Too small, Too big, You win): ").strip()
        if response == "Too small":
            min_val = guess + 1
        elif response == "Too big":
            max_val = guess - 1
        elif response == "You win":
            print(f"I've guessed your number in {attempts + 1} attempts!")
            return
        else:
            print("Wrong input!")

        attempts += 1

    print("I couldn't guess the number in 10 attempts. Please try again!")


if __name__ == "__main__":
    while True:
        try:
            guess_number()
            play_again = input("Do you want to play again? (yes/no) ").strip().lower()
            if play_again != "yes":
                print("Thanks for playing! Goodbye.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Restarting the game...")
