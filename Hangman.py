## Hangman.py
## Name: Andrew Ayers
## April 10th, 2017

#Assingment was for partial functionality, hence the last method
#being commented out

import random

def openWords(infile):
    file = open(infile, "r")
    words = []
    for line in file:
        lower = line.lower()
        word = lower.split()
        words += word[0:]
    return words

def randomPick(words):
    secretWord = random.choice(words)
    return secretWord

def underscore(secretWord):
    underscores = []
    for i in range(len(secretWord)):
        underscores += "-"
    return underscores

def guess(guess):
    guess = input("Guess a letter - ")
    guess = guess.lower()
    if ord(guess) >= 97 and ord(guess) <= 122:
        letters += guess
        return letters
    else:
        print("Not a valid entry!")

def guessed(letters, secretWord):
    

##def spelled(letters, secretWord):
##    if 
##    

##def playGame():
##    print("Welcome to Hangman!")
##    words = openWords("wordlist.txt")
##    secretWord = randomPick(words)
##    print(secretWord)
##    underscores = underscore(secretWord)
##    print("Your word =  ", end = "")
##    for item in underscores:
##        print(item, end = " ")
##    print()

    
    
   
playGame()