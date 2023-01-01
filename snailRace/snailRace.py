import random
import time
import sys

# Constants
MAX_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40


def main():
    print('\nWelcome to Snail Race.\n')

    # Valid number of snails to race
    while True:
        response = input('How many snails do you want to race?\n> ')
        if response.isdecimal():
            numSnail = int(response)
            if 1 < numSnail <= MAX_SNAILS:
                break
        print('Enter a valid number between 2 and', MAX_SNAILS)

    # Snail names
    snailNames = []
    for i in range(1, numSnail + 1):
        # Enter a valid name
        while True:
            print(f'Enter snail # {i}\'s name:')
            name = input('> ')
            if len(name) == 0:
                print('Please enter a valid name.')
            elif name in snailNames:
                print('Choose a name that is not already used.')
            else:
                break
        snailNames.append(name)

    # Start line
    print('\n'*40)  # Clear screen
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
    snailProgress = {}

    for snail in snailNames:
        print(snail[:MAX_NAME_LENGTH])
        print('@v')
        snailProgress[snail] = 0
    # Pause before race starts
    time.sleep(1.5)

    # Main game loop
    while True:
        for i in range(random.randint(1, numSnail // 2)):
            randomSnail = random.choice(snailNames)
            snailProgress[randomSnail] += 1
            if snailProgress[randomSnail] == FINISH_LINE:
                print(f'{randomSnail} has WON!')
                sys.exit()

        time.sleep(0.5)
        print('\n'*40)

        print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
        print('|' + (' ' * (FINISH_LINE - 1) + '|'))

        # Display the snails (with name tags):
        for snail in snailNames:
            spaces = snailProgress[snail]
            print((' ' * spaces) + snail[:MAX_NAME_LENGTH])
            print(('.' * snailProgress[snail]) + '@v')


if __name__ == '__main__':
    main()
