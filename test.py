import random
with open("/usr/share/dict/words") as opened_file:
    word_list = (opened_file.read().upper().split())
    secret_word = list(random.choice(word_list))

welcome_player = input("Welcome to the secret word game. There are {} letters in the secret word. "
                       "Guess a letter:  ".format(len(secret_word)))

bad_guess = []
correct_guess = []

def track_guess(bad_guess, correct_guess, secret_word):
        for letter in bad_guess:
            bad_guess.append()
            print('\n\n')

        for letter in secret_word:
            if letter in correct_guess:
                print(letter, end='')
            else:
                print('_', end='')
                print('')

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











