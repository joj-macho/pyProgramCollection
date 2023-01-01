import random
import pyperclip


def main():
    print('\nsPonGeCaSe.\n')

    message = englishToSpongecase(input('Enter you Message here.\n> '))
    print(message)

    pyperclip.copy(message)
    print('Message copied.')


def englishToSpongecase(message):
    '''This function takes a string as an input and returns a spongecase string format'''
    spongecase = ''
    useUpper = False

    for char in message:
        if not char.isalpha():
            spongecase += char
            continue
        if useUpper:
            spongecase += char.upper()
        else:
            spongecase += char.lower()

        if random.randint(1, 100) <= 90:
            useUpper = not useUpper
    return spongecase


if __name__ == '__main__':
    main()
