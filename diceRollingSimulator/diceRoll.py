import random

# Constants
DICE_FACES = {
    1: (
        '+-------+',
        '|       |',
        '|   O   |',
        '|       |',
        '+-------+'
    ),
    2: (
        '+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'
    ),
    3: (
        '+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'
    ),
    4: (
        '+-------+',
        '| O   O |',
        '|       |',
        '| O   O |',
        '+-------+'
    ),
    5: (
        '+-------+',
        '| O   O |',
        '|   O   |',
        '| O   O |',
        '+-------+'
    ),
    6: (
        '+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'
    )
}
DICE_HEIGHT = len(DICE_FACES[1])


def main():
    print('Dice Rolling Simulator\n')

    # Prompt user to choose number of dice to roll
    while True:
        response = input('How many dice do you want to roll (max 6 dice)?\n> ')
        
        if response.isdigit() and 0 < int(response) <= 6:
            numOfDice = int(response)
            break
        else:
            print('Enter a valid number of dice to roll!')
    
    # Roll the dice using the random module.
    diceRollResult = [random.randint(1, 6) for _ in range(numOfDice)]
    # print(diceRollResult)
    # Display Dice Faces
    displayFaces = generateDiceFaces(diceRollResult)
    print('RESULTS:')
    print(displayFaces)


def generateDiceFaces(diceRollResult):
    '''This function returns ASCII characters of a rolled die'''
    diceFace = [DICE_FACES[face] for face in diceRollResult]
    # print(diceFace)
    # List of dice face rows
    diceFaceRows = []
    for row in range(DICE_HEIGHT):
        rowItem = []
        for die in diceFace:
            rowItem.append(die[row])
        rowText = ' '.join(rowItem)
        diceFaceRows.append(rowText)

    diceFaceShow = '\n'.join(diceFaceRows)

    return diceFaceShow


if __name__ == '__main__':
    main()