import random

# List of predefined words
words = ["python", "computer", "hangman", "program", "keyboard"]

# Select a random word

word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===== Welcome to Hangman =====")

while wrong_guesses < max_wrong:
    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is fully guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

else:
    print("\nGame Over!")
    print("The correct word was:", word)
