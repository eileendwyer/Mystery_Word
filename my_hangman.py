#  /usr/share/dict/words
#  random
# how many letters the computer's word contains
# user input is one guess per round case insensitive
# feedback to usr about their letter guess - Guesses = 8 max - & how many
# guesses remaining - lose a guess only if guess is incorrect
# usr feedback if they duplicate guess - print(try again)
# access letters in word by index to display the partially guessed word
# end game = guess the word, use all guesses - if yes show the word
#
import random
with open("/usr/share/dict/words") as opened_file:
    word_list = (opened_file.read().upper().split())
    secret_word = list(random.choice(word_list))

number_guesses = 1

welcome_player = input("Welcome to the secret word game. There are {} letters in the secret word. "
                       .format(len(secret_word)))
bad_guess =[]
correct_guess = []

def get_guess(bad_guess, correct_guess):
    player_guess = input("Guess a letter:  ").upper()
    if len(player_guess) != 1:
        print("You can only guess one letter per turn.")
    elif player_guess in bad_guess or correct_guess:
        print("You already guessed that letter! ")
    elif notguess.isalpha():
        print("You can only guess letters!")
    else:
        return guess
get_guess()

def track_guess(bad_guess, correct_guess, secret_word):
    for letter in bad_guess:
        print('\n\n')

    for letter in secret_word:
        if letter in correct_guess:
            print(letter, end='')
        else:
            print('_' , end='')
            print('')


    for letter in word:
        print(secret_word.append('_'))
        secret_word[0] = word[0]

        while player_guesses < 9:
            if player_guesses in secret_word:
                player_guesses = good_guesses
                print("Good guess. You have {} guesses remaining. ".format(number_guesses))
                number_guesses += 1


