import random 

word_list = ["aardvark", "baboon", "camel"]

#gameprep var
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
blank_word_arr = list("_" * len(chosen_word))
blank_word = ''.join(blank_word_arr)
game_continue = True
lives = 7
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
    else:
        blank_word = ''.join(blank_word_arr)
    if lives == 0 or blank_word == chosen_word:
        game_continue = False
#===================================================================================================#
if lives == 0:
    print("You lose!")
else:
    print("You win!")

