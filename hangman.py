'''
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
'''
import random
# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


# Feel free to use this list of ascii art for your game





HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["France", "Russia", "Italy", "Germany", "India", "Japan", "China", "Hungary", "Syria"]
words = [x.upper() for x in words]

your_word = words[random.randrange(len(words))]
letter = your_word[0:]
for letter in your_word:
    print("_", end=" ")




print(HANGMANPICS[0])
print("welcome to hangman: COUNTRY EDITION")

used_letters = []

done = False
correct_answers = 0
incorrect_answers = 0
while not done:

    letter = input("Choose a Letter: ").upper()
    if letter in used_letters:
        print("Bruh you already did that")
    if letter in your_word:
        print("Nice")
        correct_answers += 1

    if letter not in your_word:
        print("Nope")

        incorrect_answers += 1
        print(HANGMANPICS[incorrect_answers])

        used_letters.append(letter)
    if incorrect_answers == 6:
        print("YOU LOSE")
        #play_again = input("Wanna Play Again?: ").upper()
        #if play_again == "Yes":
        done = True
    if correct_answers == len(your_word):
        done = True























