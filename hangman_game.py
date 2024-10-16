import random
import wordshangman


chosen_word = random.choice(wordshangman.words)
display = []
lives = 5
for i in range(len(chosen_word)):
    display+='_'
gameover = False
while not gameover:
    guess = input("guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        #for i in range(len(chosen_word)):
        if guess == letter:
            display[position]=guess
    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            gameover=True
            print("You Lose")
            print(chosen_word)
    if '_' not in display:
        gameover=True
        print("you win")


    