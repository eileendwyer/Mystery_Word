import random
import sys

with open("/usr/share/dict/words") as opened_file:
    word_list = (opened_file.read().upper().split())
    secret_word = str(random.choice(word_list))

def welcome():
    print("Welcome to the secret word game. There are {} letters in the secret word.\n You have 8 chances to guess the word. ".format(len(secret_word)))
    print(secret_word)

    for letter in secret_word:
        print('_ ', end='')

def show_guesses():
    correct_guesses = []
    for player_guess in secret_word:
        if player_guess not in correct_guesses:
            print('_ ', end='')
        else:
            print(player_guess + ' ', end='')
            return show_guesses()

def get_guess():
    correct_guesses = []
    incorrect_guesses = []
    show_guesses()
    max_guesses = 8
    while max_guesses <= 8:
        player_guess = input("\nGuess a letter:  ").upper()
        if player_guess in secret_word:
            correct_guesses.append(player_guess)
            print("Good guess! You have {} guesses remaining. ".format(max_guesses))

        elif player_guess not in secret_word:
 # finish here  for letter in (incorrect_guesses):
                if player_guess not in incorrect_guesses:
                    incorrect_guesses.append(player_guess)
                    max_guesses -= 1

                    for player_guess in incorrect_guesses:
                        print("You already guessed that letter! ")

        elif player_guess.notisalpha():
            print("You can only guess letters!")
        else:
 # finish here           for in (player_guess):
                if != 1:
                    print("You can only guess one letter per turn.")

#def end_game():

#    correct_guesses = []
#    secret_word =
#    get_guess()

#    if max_guesses == 0:
#        print("Better luck next time! The secret word was {}. ".format(secret_word))

        sys.exit()
welcome()
show_guesses()
get_guess()
#end_game()
