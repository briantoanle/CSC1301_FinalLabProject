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
        print("|    / /\/")
        print("|      ")

    elif lifeNum == 5:
        print(" ")
        print("______")
        print("|     |")
        print("|     0")
        print("|    /|")
        print("|    / /\/")
        print("|      ")

    else:
        print(" ")
        print("______")
        print("|     |")
        print("|     0")
        print("|    /|/\/")
        print("|    / /\/")
        print("|      ")


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