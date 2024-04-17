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

    if player == 7:
        guess = input(f'the word is {wordl} letters long, you have {player} guesses left.' + f'\n\n {zero}\n{blanks}\n\n>')
        guess = guess.lower
    elif player == 6:
        guess = input(f'the word is {wordl} letters long, you have {player} guesses left.' + f'\n\n {first}\n{result}\n\n>')
        guess = guess.lower
    elif player == 5:
        guess = input(f'the word is {wordl} letters long, you have {player} guesses left.' + f'\n\n {second}\n{result}\n\n>')
        guess = guess.lower
    elif player == 4:
        guess = input(f'the word is {wordl} letters long, you have {player} guesses left.' + f'\n\n {third}\n{result}\n\n>')
        guess = guess.lower
    elif player == 3:
        guess = input(f'the word is {wordl} letters long, you have {player} guesses left.' + f'\n\n {fourth}\n{result}\n\n>')
        guess = guess.lower
    elif player == 2:
        guess = input(f'the word is {wordl} letters long, you have {player} guesses left.' + f'\n\n {fifth}\n\n\n{result}\n\n>')
        guess = guess.lower
    elif player == 1:
        guess = input(f'the word is {wordl} letters long, you have {player} guesses left.' + f'\n\n {sixth}\n\n\n{result}\n\n>')
        guess = guess.lower



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