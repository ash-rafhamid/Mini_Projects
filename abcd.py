import random

def game():
    # Define a list of words for the game
    words = ["apple", "banana", "cherry", "grape", "lemon", "orange", "strawberry"]

    while True:
        # Choose a random word from the list
        word = random.choice(words)

        # Initialize an empty string to store the player's guess
        guess = ""

        while guess != word:
            guess = input("Guess the word: ").strip().capitalize()

            if guess == word:
                print("Congrats! Your guess is correct.")
            else:
                print(f"Sorry, the correct word is '{word}'.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

game()
