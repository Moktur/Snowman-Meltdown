import ascii
import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes"""
    print(ascii.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """
    most of the game logic to calculate the mistakes
    and printing the winning or loosing message
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    while True:
        # For now, display the initial game state.
        display_game_state(mistakes, secret_word, guessed_letters)
        # Prompt user for one guess (logic to be enhanced later)
        while True:
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) > 1 or len(guess) < 1:
                print("No numbers or any signs allowed. Use a single letter.")
                continue
            else:
                break
        if guess not in secret_word:
            mistakes += 1
        print("You guessed:", guess)
        if guess in secret_word:
            guessed_letters.append(guess)
        if len(guessed_letters) == len(secret_word):
            print("Congratulation, you rescued the snowman")
            break
        elif mistakes == len(ascii.STAGES):
            print("You lost!")
            break


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]
