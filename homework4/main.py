import random

words_list = ['romania', 'germany', 'italy', 'france', 'belgium', 'hungary', 'denmark', 'sweden', 'norway']
lives = 3
# choose a random word from words_list
word = random.choice(words_list)
# dashes for each letter in a word

# wrong guess counter
wrong_guesses = 0
# our used letter
used_letters = []
current_guess = "_" * len(word)
print('WELCOME TO THE GAME', '\n')
print('try to guess the word')

def check_user_input(guess):
        _used_letters = []
        length = len(guess)
        is_it_number = guess.strip().isdigit()
        if length > 1 or guess == '' or is_it_number == True:
            print('Game Rules:'
                'you can only enter one letter at a time '
                'you Cannot use numbers....'
                'Try again')
            guess = input('Enter your letter')
            guess = guess.lower()
            add = False
            check_user_input(guess)


        else:
            add = True
            is_it_used(guess, _used_letters, add)

            pass
        return add

def is_it_used(guess, used_letters, my_add):
    while guess in used_letters:
        print('You have already entered this letter', guess)
        guess = input('Enter another letter:')
        guess = guess.lower()
        # add the entered letter to used letter list
        check_user_input(guess)
    if my_add == True:
        used_letters.append(guess)

    return used_letters, guess



while wrong_guesses < lives and current_guess != word:
    print('You have used the following letters:', used_letters)
    print('So far, the word is:', current_guess)
    guess = input('Enter your letter')
    guess = guess.lower()
    #check_user_input(guess)
    my_add = check_user_input(guess)


    if guess in word and my_add == True:
        print('That is correct!')
        # show the answer until now
        new_word = ""
        for letter in range(len(word)):
            if guess == word[letter]:
                new_word += guess
            else:
                new_word += current_guess[letter]
        current_guess = new_word

        print(new_word)


    else:
        print("THAT WAS WRONG!!!")
        wrong_guesses += 1
    is_it_used(guess, used_letters, my_add)
    #checking if the letter was entered before

if wrong_guesses == lives:
    print('YOU LOST :( !!')

else:
    print('YOU WON :) !!!')




