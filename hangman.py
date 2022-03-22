import random
from hangman_art import stages
from hangman_words import word_list
from hangman_logo import logo

print(logo)
chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}")

display = []
for letter in chosen_word:
    display.append("_")
print(display)

chosen_word_list = []
for letter in chosen_word:
    chosen_word_list.append(letter)

max_turns = len(stages) - 1

incorrect_letters = []

while display != chosen_word_list:

    guess = input("What is your guess?").lower()

    if guess in display:
        print("You have already guessed this letter!")

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    if guess not in chosen_word:
        print(stages[max_turns])
        incorrect_letters.append(guess)
        print(f"These letters are not in the word: {incorrect_letters}")
        max_turns -= 1

    if max_turns < 0:
        print("You have ran out of guesses. You lose!")
        break

    if display == chosen_word_list:
        print("Congrats! You win!")

    print(display)


