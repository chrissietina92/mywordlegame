import random
import sys
import re

f = open('/Users/chrissie/Desktop/wordlist.10000.txt','r')
contents = f.read()
wordOptions = re.findall(r'\b\w{5}\b',contents)


easyOptions = ['tears', 'named']


littleOptions = ['apple', 'tears', "names", "yours", "words", "heart", "named", "snake", "lists", "pasta", "front", "witch"]

print('WORDLE!')
print('- - - - -')
print('- - - - -')
print('- - - - -')
print('- - - - -')
print('- - - - -')
print('- - - - -')
print(' ')
print('Welcome to the game wordle.')
print('You have 6 chances to guess the randomly selected 5 letter word.')
print('If you guess a word that shares a letter with the randomly selected 5 letter word and the letter is in the same spot in both words, it will have the symbol $')
print('If you guess a word that shares a letter but the letter is not in the same spot, it will have the symbol %')
print('The letters in your guessed word that are not in the randomly selected work will have the symbol #')


randomWord = random.choice(wordOptions)
print(randomWord)
letterList = []
count = 0

for i in randomWord:
    letterList.append(i)

def wordle():
    print(' ')
    print("Guess a 5-letter word")
    x = input()
    guessedLetter = []

    if x == randomWord:
        print('You got the word, it was ' + x + '. Good job!')
        sys.exit()
    else:
        for i in x:
            print(i, end = " ")
            guessedLetter.append(i)
        print('')

        y = len(guessedLetter)

        if y == 5:
            for i in range(y):
                if guessedLetter[i] == letterList[i]:
                    guessedLetter[i] = "$"
                elif guessedLetter[i] in letterList:
                    guessedLetter[i] = "%"
                else:
                    guessedLetter[i] = "#"
            for i in range(y - 1):
                print(guessedLetter[i], end =" ")
            print(guessedLetter[-1])
            for i in range(5 - count):
                print('- - - - -')
        else:
            print('Must be 5 letters, start game again')
            sys.exit()
        

for i in range(6):
    wordle()
    count += 1
print('Bad luck, the word was ' + randomWord)
