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


def game():
    correct_guesses = []
    max_guesses =8
    while True:
        player_guess = input("\n\nGuess a letter:").upper()
        if player_guess in secret_word:
            correct_guesses.append(player_guess)
            print("Good guess! You have {} guesses remaining.\n ".format(max_guesses))
            for player_guess in secret_word:
                if player_guess not in correct_guesses:
                    print('_ ', end='')
                else:
                    print(player_guess + ' ', end='')


def guesses(player_guess):
    incorrect_guesses = []
    max_guesses = 8
    for player_guess in incorrect_guesses:
        print("\nYou already guessed that letter!")
    if player_guess not in incorrect_guesses:
        print(" Incorrect guesses: ".format(incorrect_guesses))
        incorrect_guesses.append(player_guess)
        max_guesses -= 1
    elif player_guess.notisalpha():
        print("You can only guess letters!")
        return(player_guess)
    sys.exit()

welcome()
game()
guesses(player_guess)
#        else:
# #if len(player_guess) != 1:
# print("You can only guess one letter per turn.")

# def end_game():
#    correct_guesses = []
#    secret_word =
#    get_guess()
#    if max_guesses == 0:
#        print("Better luck next time! The secret word was {}. ".format(secret_word))

# end_game()
