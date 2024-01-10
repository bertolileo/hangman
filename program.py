import random 
from hangmam_words import word_list
from game_art import logo
from game_art import stages
import os

def clear_console():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

#===================================================================================================#
#gameprep 
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
blank_word_arr = list("_" * len(chosen_word))
blank_word = ''.join(blank_word_arr)
repeated_letters = []
game_continue = True
lives = 6
#===================================================================================================#
while game_continue:
    clear_console()
    print(logo)
    print(stages[lives])
    print(blank_word)
    print("Repeated letters: " + ' - '.join(repeated_letters))
    letter = input("Guess a letter: ")
    if letter in repeated_letters:
        print("You've already tried this letter; please type a different one.")
        input()
    else:
        has_letter = False
        repeated_letters.append(letter)
        #search letter
        for i in range(0, len(chosen_word)):
            if letter == chosen_word[i]:
                has_letter = True
                blank_word_arr[i] = chosen_word[i]

        if not has_letter:
            lives -= 1
            print(f"You gessed {letter}, that's not int he word. You lose a life.")
        else:
            blank_word = ''.join(blank_word_arr)

        if lives < 0 or blank_word == chosen_word:
            game_continue = False

#===================================================================================================#
clear_console()
if lives < 0:
    print("You lose!")
    print(f"The word was: {chosen_word}")
else:
    print("You win!")
    print(f"The word was: {chosen_word}")

#===================================================================================================#
