import random
import time


def main():
    print('\nMagic Fortune Ball. \n')

    # Slow spaced print
    slowSpacePrint('Magic Fortune Ball!')
    time.sleep(0.5)
    slowSpacePrint('Ask me a Yes or No Question.')
    input('> ')

    # Display a brief reply:
    replies = [
        'LET ME THINK ON THIS...',
        'AN INTERESTING QUESTION...',
        'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
        'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
        'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
        'YES... NO... MAYBE... I WILL THINK ON IT...',
        'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
        'I SHALL CONSULT MY VISIONS...',
        'YOU MAY WANT TO SIT DOWN FOR THIS...',
    ]

    slowSpacePrint(random.choice(replies))

    slowSpacePrint('.' * random.randint(4, 12), 0.7)

    # Answer
    slowSpacePrint('I have an answer...', 0.2)
    time.sleep(1)
    answers = [
        'YES, FOR SURE',
        'MY ANSWER IS NO',
        'ASK ME LATER',
        'I AM PROGRAMMED TO SAY YES',
        'THE STARS SAY YES, BUT I SAY NO',
        'I DUNNO MAYBE',
        'FOCUS AND ASK ONCE MORE',
        'DOUBTFUL, VERY DOUBTFUL',
        'AFFIRMATIVE',
        'YES, THOUGH YOU MAY NOT LIKE IT',
        'NO, BUT YOU MAY WISH IT WAS SO',
    ]
    slowSpacePrint(random.choice(answers), 0.05)


def slowSpacePrint(text, interval=0.1):
    '''This function slowly displays text with spaces in between letters'''
    for char in text:
        if char == 'I':
            print('i', end='', flush=True)
        else:
            print(char + ' ', end='', flush=True)
        time.sleep(interval)
    print()


if __name__ == '__main__':
    main()
