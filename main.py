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
    #print(masterList[secretWord])
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

def hangmanConversion(word, letter):
  letterPosition = word.find(letter)

  for index in range(len(word)):
    if word[index] == word[letterPosition]:
        print(letter, end = " ")

    else:
        print("_", end= " ")

def main():
    # get .txt file and store it into master list
    storeWordsIntoList()

    # store the secret word inside a variable
    word = getWord()
    hangman = ''
    for i in range(len(word)):
        hangman += '-'
    print(word)
    print(hangman)

    stillGuessing = True
    while stillGuessing:
        tempChar = input('Enter your guess ')
        letterPos = word.find(tempChar)
        for i in range(len(word)):
            if tempChar == word[i]:
                hangman = hangman[:i] + word[i] + hangman[i+1:]
        print(hangman)
        if hangman == word:
            print('you won')
    print(word)
    print(hangman)

main()
