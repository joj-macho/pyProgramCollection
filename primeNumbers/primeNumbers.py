import math
import sys


def main():
    print('\nWelcome to Prime Numbers.')

    while True:
        response = input(
            'Enter a number to start searching for prime numbers from. \n> ')
        if response.isdecimal():
            num = int(response)
            break

    input('Press Enter to Continue ...')

    while True:
        if isPrime(num):
            print(str(num) + ', ', end='', flush=True)
        num += 1


def isPrime(number):
    '''This function checks if number is prime, returns True and False'''
    if number < 2:
        return False
    elif number == 2:
        return True

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
