import random

print("Welcome to Hangman Game")

word_list = ["apple", "mango", "banana", "orange", "grapes"]

secret_word = random.choice(word_list)

guessed_word = ["_"] * len(secret_word)

chances = 6

while chances > 0:

    print("\nWord:", " ".join(guessed_word))

    letter = input("Enter a letter: ").lower()

    if letter in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                guessed_word[i] = letter

        print("Correct Guess!")

    else:
        chances = chances - 1
        print("Wrong Guess!")
        print("Remaining Chances:", chances)

    if "_" not in guessed_word:
        print("\nCongratulations! You found the word:", secret_word)
        break

if "_" in guessed_word:
    print("\nGame Over!")
    print("The correct word was:", secret_word)