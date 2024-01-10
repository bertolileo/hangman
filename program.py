import random 
from hangmam_words import word_list
from game_art import logo
from game_art import stages

#gameprep var
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
blank_word_arr = list("_" * len(chosen_word))
blank_word = ''.join(blank_word_arr)
game_continue = True
lives = 6

print(logo)
print(chosen_word)
#===================================================================================================#
while game_continue:
    print(blank_word)
    letter = input("Guess a letter: ")
    has_letter = False

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
        break

    print(stages[lives])
#===================================================================================================#
if lives < 0:
    print("You lose!")
else:
    print("You win!")
    print(f"The word was: {chosen_word}")

#===================================================================================================#
