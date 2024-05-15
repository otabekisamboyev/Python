import random
from hangman_words import word_list
from hangman_art import stages, logo
'''My solution
stage_index = len(stages) - 1
list_of_word = word_list
word = random.choice(list_of_word)
word_list = []
for i in word:
    word_list.append('_')
length = len(word_list)
heart = 6
guess_chars = set()
print(logo + '\n')
print(f"Psst, spoiler: {word}")
while heart > 0 and length > 0:
    char = input("Guess the letter: ")
    if char in word:
        print(f"You guessed {char}, that's in the word.")
        if char not in guess_chars:
            for i in range(len(word)):
                if char == word[i]:
                    word_list[i] = word[i]
                    length -= 1
        else:
            print("You have already found this letter!")
        for n in word_list:
            print(n, end=" ")
        print(stages[stage_index])
    else:
        print(f"You guessed {char}, that's not in the word. You lose a life")
        stage_index -= 1
        for n in word_list:
            print(n, end=" ")
        print(stages[stage_index])
        heart -= 1
    guess_chars.add(char)
if length == 0 and heart > 0:
    print(f"You found the word: {word}. You win!")
else:
    print(f"You couldnt find the word: {word}. You loose!")
'''

'''Teacher's solution'''
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
