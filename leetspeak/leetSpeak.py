import random
# import pyperclip


def main():
    print('/nW3lc0m3 T0 L3375P34K. \n')

    english = input('Enter your leet Message:\n> ')
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        pyperclip.copy(leetspeak)
        print('Text Copied.')
    except NameError:
        pass


def englishToLeetspeak(message):
    '''This function converts English string and returns Leetspeak string.'''
    charMapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/']}
    leetspeak = ''

    for char in message:
        if char.lower() in charMapping and random.random() <= 0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak += leetReplacement

        else:
            leetspeak += char

    return leetspeak


if __name__ == '__main__':
    main()
