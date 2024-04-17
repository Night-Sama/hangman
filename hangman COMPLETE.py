import os
import time
import random

words = ['pony', 'psycho', 'ant', 'art', 'player', 'arrive']
word = random.choice(words)
wordl = len(word)
lword = list(word)
player = 7
result = ''
guesses = []
blanks = '_' * wordl


zero = '''

|
|
|
|

'''

first = '''
______
|     |
|
|
|

'''

second = '''
______
|     |
|     O
|
|

'''

third = '''
______
|     |
|     O
|     |
|

'''

fourth = '''
______
|     |
|     O
|    /|
|

'''

fifth = '''
______
|     |
|     O
|    /|\ ''' + '\n|'

sixth = '''
______
|     |
|     O
|    /|\ ''' + '\n|    /'

final = '''
______
|     |
|     O
|    /|\ \n|    / ''' + '\ '



while player > 0:

    if 1 <= player <= 7:
        guess_prompt = f'the word is {wordl} letters long, you have {player} guesses left.'
        if player > 1:
            guess_prompt += f'\n\n {"".join([sixth, f"\n{result}\n", fifth, fourth, "", ""][1:player+1])}'
        guess = input(guess_prompt).lower()




    if guess is int or guess is float:
        print('invalid option, that is not a word')
        time.sleep(1.4)
        os.system('cls')
    elif len(guess) > wordl:
        print('Invalid option, word too long')
        time.sleep(1.4)
        os.system('cls')

    elif player >= 0:
        for i in guess:
            if i in lword:
                guesses.append(i)
        result = ''
        for i in lword:
            if i in guesses:
                result = result + i
            else:
                result = result + '_'
        if guess == word:
            print('You win!')
            break
        elif guess != word:
            if player != 0:
                print('Incorrect guess.')
                player = player - 1
                if player > 0:
                    time.sleep(0.5)
                    print("Try again.")
                    time.sleep(1)
                    os.system('cls')
                else:
                    time.sleep(1)
                    os.system('cls')
                    print(final + f'\n\n\n{result}' + "\n\nYou lose! you're out of guesses.\n")
                    break
