import sys


def main():
    print('\nFibonacci Sequence Generator.\n')

    while True:
        # Enter a valid input
        while True:
            response = input(
                'Enter the nth Fibonacci number to compute. Press (q)uit to quit.\n> ').lower()
            if response == 'q' or response == 'quit':
                print('Bye!')
                sys.exit()
            if response.isdecimal() and int(response) > 0:
                n = int(response)
                break

            print('Enter a positive number or (q)uit.')

        # 1 or 2
        if n == 1:
            print('0 \n#1 Fibonacci number is 0.')
            continue
        elif n == 2:
            print('0, 1 \n#2 Fibonacci number is 1.')
            continue

        # large numbers
        if n >= 10000:
            input('Warning! This will take a while to display on screen. \nPress Ctrl-C to quit. \nPress Enter to begin...')

        # Calculate Fibonacci
        secondToLastNumber = 0
        lastNumber = 1
        calculatedFib = 2
        print(f'First {n} Fibonacci Numbers:')
        print('0, 1, ', end='')

        while True:
            nextNumber = secondToLastNumber + lastNumber
            calculatedFib += 1
            print(nextNumber, end='')

            if calculatedFib == n:
                print()
                print(
                    f'\nThe #{calculatedFib} Fibonacci number is {nextNumber}', sep='')
                print()
                break

            print(', ', end='')

            secondToLastNumber, lastNumber = lastNumber, nextNumber


if __name__ == '__main__':
    main()
