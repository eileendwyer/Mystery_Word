#  random
#  /usr/share/dict/words
import random
with open("/usr/share/dict/words") as opened_file:
    word_list = (opened_file.read().upper().split())
    secret_word = list(random.choice(word_list))
    secret_word[0] = word_list[0]
# how many letters the computer's word contains
welcome_player = input("\nWelcome to the secret word game. There are {} letters in the secret word. "
                       .format(len(secret_word)))
def get_guess():
    # user input is one guess per round case insensitive
    # feedback to usr about their letter guess - Guesses = 8 max - & how many
    secret_word = []
    incorrect_guess = []
    repeat_guess = []
    max_guesses = 8

    player_guess = input("Guess a letter:  ").upper()
 # guesses remaining
    if player_guess in len(secret_word):
        print(secret_word.append('_'))
 # show correct guesses
        print("Good guess! You have {} guesses remaining. ".format(max_guesses))
# lose a guess only if guess is incorrect
    elif player_guess not in secret_word or repeat_guess:
        incorrect_guess.append(player_guess)
        max_guesses -=1
 # usr feedback if they duplicate guess - print(try again)
    elif player_guess in repeat_guess or incorrect_guess and player_guess not in secret-word:
        repeat_guess.append(player_guess)
        print("You already guessed that letter! ")

    elif len(player_guess) != 1:
        print("You can only guess one letter per turn.")

    elif player_guess.notisalpha():
        print("You can only guess letters!")
    else:
        return player_guess

def track_guess(secret_word, incorrect_guess, correct_guess):
    for letter in incorrect_guess:
        print('\n\n')

    for letter in secret_word:
        if letter in correct_guess:
            print(letter, end='')
        else:
            print('_' , end='')
            print('')
# end game = guess the word, use all guesses - show the word
def game_over():

            get_guess()
            game_over()

