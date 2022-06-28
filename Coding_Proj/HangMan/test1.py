
import random
from hangman_words import word_list
from HangMan.hangman_arts import stages

# TO-DO 1: Randomly choose a word from the word list


word_choices = word_list

magic_word= ""
lives = 6

# index = random.randint(0,2) #can use random.choice(word_choices)
# magic_word = word_choices[index]
# instead of using random.randint, we can use random.choice to get the random word


from HangMan.hangman_arts import logo
print(logo)

magic_word = random.choice(word_choices)
num_guesses = len(magic_word)

print(magic_word)



# TO-DO 2: From the magic_word, determine its length and ask for user input xtimes according to the length
display = []
for i in range(num_guesses):
    display.append("")

# for i in range(num_guesses):

end_of_game = False
while not end_of_game:
    guess = input("Guess the word!").lower()

    for i in range(len(magic_word)):
        letter = magic_word[i]
        if letter == guess:
            display[i] = letter # cannot use insert here if u insert it will push back one by one to the back

    print(display)

    if guess not in magic_word:
        print(f'You guessed {guess}, that is not in the word. You lose a life!')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')
    else:
        if guess in display:
            print(f'You already guessed {guess}')

    print(f"{' '.join(display)}")

    if "" not in display:
        end_of_game = True
        print('You win')

    print(stages[lives])

   













