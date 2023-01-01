import sys
import time


def main():
    print('\nThe Collatz Sequence.\n')
    # Enter a valid integer value.
    while True:
        response = input(
            'Enter a number greater than 0 or (q)uit to exit.\n> ').lower()

        if response.startswith('q'):
            print('Bye!')
            sys.exit()
        if (not response.isdecimal()) or response == 0:
            print('Enter a valid integer greater than 0')
        else:
            break

    n = int(response)
    print(f'\nCollatz Sequence starting from {n}:')
    print(n, end='', flush=True)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1

        print(f', {n}', end='', flush=True)

        time.sleep(0.1)

    print()


if __name__ == '__main__':
    main()
