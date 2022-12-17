#HANGMAN GAME WITH PYTHON

import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
import hangman_art
print(hangman_art.logo)

#Testing code

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    if guess == display:
      print(f"The letter guessed is {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        
        print(f"The letter guessed is {guess}, but its not in the word, so you lost a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'And the word is {chosen_word}.')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    from hangman_art import stages
    print(stages[lives])
