import json

import requests
'''
Program: CS 1301 Lab 11
Author: Ali Vafaeian and Toan Lee

Purpose:
    Create a hangman video game that uses everything we have learned so far this year

Pre-conditions:
    Generate a random word from a text file that contains many words.
    Take in an input from the user which is their guess of a letter in that word.
        Make sure that they enter a valid character, specifically a letter.


Post-conditions:
    Print the list of random numbers in a test.txt file and the prime number inside of prime.txt file
    Print everything inside of the window as well to make testing easier
'''
import random

masterList = []


# Read text file and store words into list
def storeWordsIntoList():
    # List of 58109 words
    with open('wordlist.txt', 'r') as f:
        for line in f:
            temp = line.strip()
            masterList.append(temp)


# Get a random word from master list
def getWord():
    secretWord = random.randint(0, len(masterList) - 1)
    return masterList[secretWord]


# Makes sure that the user enters only a single character that is a letter and if not it asks the user to re-enter a character
def inputValidation(inputStr):
    specialCharacter = "[@_!#$%^&*()<>?/|}{~:]',."
    if len(inputStr) > 1:
        print('Please enter one character only. ')
        return 0
    elif inputStr.isdigit():
        print('Please enter a letter only. ')
        return 0
    elif inputStr in specialCharacter:
        print('Please enter a letter only. ')
        return 0
    else:
        return inputStr

# Get API from dictionaryapi and return the definition
def getAPI(word):
    webString = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    #response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/life")
    response = requests.get(webString)
    text = response.json()
    #print(text)
    meaning = text[0]['meanings'][0]['definitions'][0]['definition']
    return meaning


# Updates the graphic of the hangman depending on the number of errors the user has made
def hangmanGraphic(lifeNum):
    if lifeNum == 0:
        print(" ")
        print("_______")
        print("|     |")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")

    elif lifeNum == 1:
        print(" ")
        print("_______")
        print("|     |")
        print("|     0")
        print("|      ")
        print("|      ")
        print("|      ")


    elif lifeNum == 2:
        print(" ")
        print("_______")
        print("|     |")
        print("|     0")
        print("|     |")
        print("|      ")
        print("|      ")

    elif lifeNum == 3:
        print(" ")
        print("_______")
        print("|     |")
        print("|     0")
        print("|     |")
        print("|    / ")
        print("|      ")

    elif lifeNum == 4:
        print(" ")
        print("_______")
        print("|     |")
        print("|     0")
        print("|     |")
        print("|    / \\")
        print("|      ")

    elif lifeNum == 5:
        print(" ")
        print("_______")
        print("|     |")
        print("|     0")
        print("|    /|")
        print("|    / \\")
        print("|      ")

    else:
        print(" ")
        print("_______")
        print("|     |")
        print("|     0")
        print("|    /|\\")
        print("|    / \\")
        print("|      ")


def main():
    # get .txt file and store it into master list
    storeWordsIntoList()

    # store the secret word inside a variable
    word = getWord()

    # Generates the blank lines that represent the letters in the word
    hangman = ''
    for i in range(len(word)):
        hangman += '_'

    # Initializes the variables like the life numner, number of correct guesses, number of wrong guesses, and whether or not the user is still guessing
    correct = 0
    wrong = 0
    life = 0
    stillGuessing = True

    wrongCharList=[]
    alreadyEntered = []
    # While the user is still guessing
    while stillGuessing:
        # Used for debugging to easily know what the word is
        # print(word)

        # Prints the initial graphic as well as the initial number of letters in the word
        hangmanGraphic(life)
        print()
        print(hangman)

        # Takes in the user input and ensures it is only a single letter
        userInput = input('Enter your guess ')
        in1 = inputValidation(userInput)

        charList = ''
        for k in alreadyEntered:
            charList += k.upper() + ' '
        if in1 == userInput:
            print("You have already entered " + charList )
            # If the letter guessed is not in the word then the life increases by 1 and the graphic updates
            if in1 in wrongCharList or in1 in alreadyEntered:
                print(f"You already entered '{in1}'")
            elif in1 not in word:
                life += 1
                wrongCharList.append(in1)
            # The blank letters are to be updated if a correct letter is guessed from the word
            else:
                for i in range(len(word)):
                    if userInput == word[i]:
                        hangman = hangman[:i] + word[i] + hangman[i + 1:]
                        correct += 1
                    else:
                        wrong += 1
            #print('life',life,'hang',hangman[0])

            if life == 2 and hangman[0] == '_':
                print('Hint 1: the first character in this word is',word[0])
            elif life == 3:
                print('Hint 2: the meaning of this word is: ')
                print(getAPI(word))

            alreadyEntered.append(in1)
        print(hangman)

        # Once the hangman underlined word equals the original word then the game is over and the user wins
        if hangman == word:
            print('You won\n')
            stillGuessing = False

        # If the entire hangman drawing is completed the game is over and the user looses
        if life == 6:
            hangmanGraphic(life)
            print("You lost!")
            print('The word is',word)
            stillGuessing = False



# The game will infinitely run until the user wants to stop
def playGame():
    while True:
        print('***********************************************')
        userChoice = input("Do you want to play the hangman game? (Y)es (N)o: ")
        if userChoice == "y" or userChoice == '1':
            main()
            continue
        else:
            print("Goodbye.")
            break

playGame()
