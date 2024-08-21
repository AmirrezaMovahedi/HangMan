import random
from collections import Counter
import requests

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

words = someWords.split(' ')
word = random.choice(words)

url = 'https://www.fruityvice.com/api/fruit/all'
response = requests.get(url)

if response.status_code == 200:
    someWords = []
    for fruit in response.json():
        someWords.append(fruit['name'].lower())
    word = random.choice(someWords)

if __name__ == '__main__':
    print('welcome to hangman game', 'try to guess word HINT: word is fruit')

    for _ in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while flag == 0 and chances != 0:
            chances -= 1
            try:
                guess = str(input('Enter a word to guess: '))

            except:
                print('please enter just a letter!')
                continue
            if len(guess) > 1:
                print('please enter single letter!')
                continue
            elif not guess.isalpha():
                print('please enter a letter!')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
                for char in word:
                    if Counter(letterGuessed) != Counter(word) and char in letterGuessed:
                        print(char, end=' ')
                        correct += 1
                    elif Counter(letterGuessed) == Counter(word):
                        print('the game is finished, you won!!')
                        flag = 1
                        print(f'word: {word}')
                        break
                    else:
                        print('_', end=' ')
        if chances <= 0 and Counter(word) != Counter(letterGuessed):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('bye try again!')
        exit()
