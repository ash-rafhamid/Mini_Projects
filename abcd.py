import random

lettergit m_letter}: ").strip().capitalize()

        if guess == word:
            print("Congrats! Your guess is correct.")
        else:
            print(f"Sorry, the correct word is '{word}'.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break


game()