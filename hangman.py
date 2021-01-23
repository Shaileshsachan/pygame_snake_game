import random
import wordlist

chosen_word = random.choice(wordlist.words)

lives = 6
display = []
for letter in chosen_word:
    display +='-'
print(display)

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You Lose')
    if '-' not in display:
        end_of_game = True
        print('You win')