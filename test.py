import random
word_list = ['abruptly', 'absurd', 'abyss', ]
chosen_word = random.choice(word_list).lower()
print(chosen_word)
word_length = len(chosen_word)
display = []
not_display = []
lives = 6
end = False

for _ in range(word_length):
    display += "_"
print(display)

while not end:
    guess = input("Guess the letter: ").lower()
    
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter            
    print(display)
    if not "_" in display:
        end = True
    
    if not guess in not_display and guess not in chosen_word:
        if not guess in not_display:
            not_display.append(guess)
        lives -= 1
        if lives == 0:
            end = True
            print("You lose")
    else:
        if not guess in not_display:
            not_display.append(guess)
    print(f"Guessed {not_display}" )
        
    print("not display", lives)