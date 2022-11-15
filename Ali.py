def hangmanConversion(word, letterList):
    length = len(word)
    for letter in letterList:
        letterPosition = word.find(letter)
        for index in range(length):
            if word[index] == word[letterPosition]:
                print(letter, end=" ")
                print('here')
            else:
                print("_", end=" ")


'''
Game Plan:
 -
'''
import random

masterList = []

# read text file and store words into list
def storeWordsIntoList():

    # list of 58109 words
    with open('wordlist.txt','r') as f:
        for line in f:

            temp = line.strip()
            masterList.append(temp)

# get a random word from master list
def getWord():
    secretWord = random.randint(0,len(masterList)-1)
    return masterList[secretWord]


def guessing():
    hangman = ''
    word = 'alibaba'
    for i in range(len(word)):
        hangman+='-'
    for i in range(len(word)):
        if 'a' == word[i]:
            hangman = hangman.replace('-','a')

    stillGuessing = True
    while stillGuessing:
        tempChar = str(input("Please enter the character you want to guess:"))

def inputValidation(inputStr):
    if len(inputStr) > 1:
        print('Please enter one character only. ')
        return 0
    elif inputStr.isdigit():
        print('Please enter a character. ')
        return 0
    else:
        return inputStr
def hangmanGraphic(lifeNum):
    if lifeNum == 0:
        print(" ")
        print("______")
        print("|     |")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")

    elif lifeNum == 1:
        print(" ")
        print("______")
        print("|     |")
        print("|     0")
        print("|      ")
        print("|      ")
        print("|      ")


    elif lifeNum == 2:
        print(" ")
        print("______")
        print("|     |")
        print("|     0")
        print("|     |")
        print("|      ")
        print("|      ")

    elif lifeNum == 3:
        print(" ")
        print("______")
        print("|     |")
        print("|     0")
        print("|     |")
        print("|    / ")
        print("|      ")

    elif lifeNum == 4:
        print(" ")
        print("______")
        print("|     |")
        print("|     0")
        print("|     |")
        print("|    / \\")
        print("|      ")

    elif lifeNum == 5:
        print(" ")
        print("______")
        print("|     |")
        print("|     0")
        print("|    /|")
        print("|    / \\")
        print("|      ")

    else:
        print(" ")
        print("______")
        print("|     |")
        print("|     0")
        print("|    /|\\")
        print("|    / \\")
        print("|      ")

from IPython.display import clear_output

def main():
    # get .txt file and store it into master list
    storeWordsIntoList()

    # store the secret word inside a variable
    word = getWord()

    hangman = ''
    for i in range(len(word)):
        hangman += '-'

    correct = 0
    wrong = 0
    life = 0
    stillGuessing = True
    while stillGuessing:
        
        # Used for debugging to easily know what the word is
        # print(word)
        hangmanGraphic(life)
        print(hangman)
        userInput = input('Enter your guess ')
        in1 = inputValidation(userInput)
        if in1 == userInput:
            if in1 not in word:
                life += 1
            for i in range(len(word)):
                if userInput == word[i]:
                    hangman = hangman[:i] + word[i] + hangman[i+1:]
                    correct +=1
                else:
                    wrong+=1
        print(hangman)

        if hangman == word:
             print('You won!')
             stillGuessing = False
        if life == 6:
            hangmanGraphic(life)
            print("You lost!")
            stillGuessing = False


from os import system, name

# import sleep to show output for some time period
from time import sleep


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

main()


def hangmanGuess(word):
    # Initial printing of the hangman as well as the word in underline form
    hangmanGraphic(0)
    hangmanConversion(word, "1")
    correctLetterList = []
    wrongLetterList = []

    life = 0

    while True:
        letter = input("Enter a letter: ")

        if letter in word:
            correctLetterList.append(letter)
            hangmanGraphic(life)
            hangmanConversion(word, correctLetterList)
            continue

        else:
            life += 1
            hangmanGraphic(life)
            hangmanConversion(word, letter)
            if life == 5:
                break
            else:
                wrongLetterList.append(letter)
                continue


UserChoice = int(input("Do you want to play the hangman game? (1)Yes (2)No: "))
if UserChoice == 1 or UserChoice == 'y':
    hangmanGuess("dog")
else:
    print("Goodbye.")