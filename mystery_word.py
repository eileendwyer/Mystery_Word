import random
import sys

with open("/usr/share/dict/words") as opened_file:
    word_list = (opened_file.read().upper().split())
    secret_word = str(random.choice(word_list))


def welcome():

    print("Welcome to the secret word game. There are {} letters in the secret word."
          "\n\nYou have 8 chances to guess the word.\n ".format(len(secret_word)))

    print(secret_word)
    for letter in secret_word:
        print('_ ', end='')


def show_guesses():
    for player_guess in secret_word:
        if player_guess not in correct_guesses:
            print('_ ', end='')
        else:
            print(player_guess + ' ', end='')

correct_guesses = []
incorrect_guesses = []
total_guesses = []
max_guesses = 8

welcome()
while max_guesses <= 8:
    show_guesses()
    player_guess = input("\n\nGuess a letter:").upper()
    if len(player_guess) > 1:
        print("You can only guess one letter at at time!")
    if player_guess in total_guesses:
        print("\nYou already guessed that letter!")
    if player_guess in secret_word:
        correct_guesses.append(player_guess)
        total_guesses.append(player_guess)
        print("Good guess! You have {} guesses remaining.\n ".format(max_guesses))
    else:
        incorrect_guesses.append(player_guess)
        total_guesses.append(player_guess)
        max_guesses -= 1
else:
    if max_guesses == 0:
        print("Better luck next time! The secret word was {}. ".format(secret_word))
    elif len(correct_guesses) == len(secret_word):
        print("Congratulations! You guessed the secret word!")
    else:
        play_again = input("Do you want to play again? Y/n").lower()
        if play_again != 'n':
            welcome()
        else:
            print("Bye!")
        sys.exit()