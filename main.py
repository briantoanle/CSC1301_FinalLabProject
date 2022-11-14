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
    stillGuessing = True
    while stillGuessing:
        print(word)
        print(hangman)
        userInput = input('Enter your guess ')
        in1 = inputValidation(userInput)
        if in1 == userInput:

            for i in range(len(word)):
                if userInput == word[i]:
                    hangman = hangman[:i] + word[i] + hangman[i+1:]
                    correct +=1
                else:
                    wrong+=1
                    print('here')
        print('corr',correct)
        print(hangman)
        if hangman == word:
            stillGuessing = False

    print('you won')
    #print(word)
    #print(hangman)

#main()
