import math
import shutil
import sys
import time

# Constants
WIDTH, HEIGHT = shutil.get_terminal_size()
WIDTH -= 1


def main():
    print('\nWelcome to Sine Message.')

    while True:
        message = input(
            f'What message do you want to display?. \nMaximum {WIDTH // 2} characters.\n> ')
        if 1 <= len(message) <= (WIDTH // 2):
            break
        print(f'Message must be  to {WIDTH //2} characters long.')

    step = 0
    multiplier = (WIDTH - len(message)) / 2
    try:
        while True:  # Main program loop.
            sinOfStep = math.sin(step)
            padding = ' ' * int((sinOfStep + 1) * multiplier)
            print(padding + message)
            time.sleep(0.1)
            step += 0.25  # (!) Try changing this to 0.1 or 0.5.
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.


if __name__ == '__main__':
    main()
