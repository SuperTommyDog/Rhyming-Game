import random
import os
import time

# Variables
startingWord = ["Cat", "Fan", "Sort", "Game"]
guessedWords = []
score = 0


def fileEditing():
    wordsFile = os.path.exists('./startingWords.txt')
    if wordsFile is False:
        with open("startingWords.txt", "w") as txt_file:
            for line in startingWord:
                txt_file.write("".join(line) + "\n")
        print("Created the Starting words file!")
    else:
        print("The starting words file already exists!")


def deleteStartingWord(word):
    with open("startingWords.txt", "r") as input:
        with open("temp.txt", "w") as output:
            for line in input:
                if word not in line.strip("\n"):
                    output.write(line)

    # replace file with original name
    os.replace('temp.txt', 'startingWords.txt')
    print("Successfully deleted " + word)
    print("The current starting words are:")
    file = open("startingWords.txt")
    print(file.read())
    file.close()


def addStartingWord(word):
    startingWord.append(word)
    print("Added " + word + " To the list of starting words!")
    time.sleep(1)
    f = open("startingWords.txt", "a")
    f.write(word + "\n")
    f.close()
    print("The current starting words are:")
    file = open("startingWords.txt")
    print(file.read())
    file.close()
    addWordOption()


# Checking necessary folders / data bases exist before going further!
def startUp():
    wordsFile = os.path.exists('./words.txt')
    if wordsFile is False:
        print("Please install the other files on the GitHub repo!")
    else:
        print("Please choose and option to proceed!")
        print("(1) See all the starting words")
        print("(2) Start the game")
        option = int(input("Please select and option "))
        if option == 1:
            print("The current starting words are:")
            file = open("startingWords.txt")
            print(file.read())
            file.close()
            time.sleep(1)
            addWordOption()


def addWordOption():
    print("")
    print("What do you want to do now?")
    print("(1) Add a word")
    print("(2) Delete a word")
    print("(3) Start the game")
    option = int(input("Please select an option "))
    if option == 1:
        newWord1 = input("Please enter a new word to add! ")
        addStartingWord(newWord1)
    if option == 2:
        deleteWord = input("Please enter the word to delete! ")
        deleteStartingWord(deleteWord)
    if option == 3:
        print("Starting game!")


def checkRhyme(word1, word2):
    a = 0
    b = 0

    # Checking word 1
    for character in word1:
        a += 1
    check1 = (a - a) + 2
    word1 = word1[::-1]
    output1 = word1[:check1]

    # Checking word 2
    for character in word2:
        b += 1
    check2 = (b - b) + 2
    word2 = word2[::-1]
    output2 = word2[:check2]

    # Checking to see if they rhyme
    if output1 == output2:
        return True
    else:
        return False


def play():
    global newWord, nextWord
    if checkRhyme(nextWord, newWord) is True:
        nextWord = input("Please enter a word that rhyme with " + nextWord + "! ")
        print(guessedWords)
    else:
        print("You lost")


fileEditing()
startUp()
startWord = random.choice(startingWord)
newWord = input("Please enter a word that rhyme with " + startWord + "! ")
if checkRhyme(startWord, newWord) is True:
    nextWord = input("Please enter a word that rhyme with " + newWord + "! ")
    play()
else:
    print("You lost")
