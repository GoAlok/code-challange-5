import random
from hangman_words import word_list
from hangman_arts import logo, stages

# Variables
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
lives = 6
end_of_game = False
not_display = []
display = []

stamp = logo
print(stamp)
# Testing Code
print(chosen_word)
# Create and displaying blanks
for _ in range(word_length):
    display += "_"
print(display)

# Game logic
while not end_of_game:
    guess = input("Guess the letter: ").lower()

    # Check Guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess} ")
        if letter == guess:
            display[position] = letter
            lives = lives
    if not guess in not_display and guess not in chosen_word:
      if not guess in not_display:
        not_display.append(guess)
        lives -= 1
        if lives == 0:
          end_of_game = True
          print("You lose")
    else:
      if not guess in not_display:
        not_display.append(guess)
    if lives > 0:
      print(f"Word is {' '.join(display)}. Lives left: {lives} ")
    else:
      print(f"The word was '{chosen_word.capitalize()}' and you failed. Lives left: {lives} ")
    
    # Check if user got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"You win!!! The word is '{chosen_word.capitalize()}'.")
    print(stages[lives])