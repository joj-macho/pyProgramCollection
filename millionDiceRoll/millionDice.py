import random
import time


def main():
    print('\nMillion Dice Roll Simulator.')
    print('This program generates a million simulations of rolling n dices and gives you the percentage of the dice total.')

    numberOfDice = int(input('Enter the number of Dice:\n> '))
    # Store dice roll results
    results = {}
    for i in range(numberOfDice, (numberOfDice*6) + 1):
        results[i] = 0

    # Dice Roll Simulation
    print(f'Simulating 1 000 000 rolls of {numberOfDice} dice.')
    lastPrint = time.time()
    for i in range(1000000):
        if time.time() > lastPrint + 1:
            print('{0}% done ...'.format(round(i/10000, 1)))
            lastPrint = time.time()

        total = 0
        for j in range(numberOfDice):
            total += random.randint(1, 6)
        results[total] += 1

    # Show results
    print('--'*15)
    print('Total - Rolls - Percentage')
    print('--'*15)

    for i in range(numberOfDice, (numberOfDice*6) + 1):
        roll = results[i]
        percentage = round(results[i] / 10000, 1)
        print('  {} - {} rolls - {}%'.format(i, roll, percentage))


if __name__ == '__main__':
    main()
