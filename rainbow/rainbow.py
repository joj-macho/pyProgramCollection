import time
import sys
import bext


def main():
    print('\nWelcome to The Rainbow Simulation.')

    input('Press enter to Continue ...')

    indent = 0
    indentIncrease = True

    try:
        while True:
            print(' ' * indent, end='')
            bext.fg('red')
            print('##', end='')
            bext.fg('yellow')
            print('##', end='')
            bext.fg('green')
            print('##', end='')
            bext.fg('blue')
            print('##', end='')
            bext.fg('cyan')
            print('##', end='')
            bext.fg('purple')
            print('##')

            if indentIncrease:
                # Increase the number of spaces:
                indent = indent + 1
                if indent == 60:  # (!) Change this to 10 or 30.
                    # Change direction:
                    indentIncrease = False
            else:
                # Decrease the number of spaces:
                indent = indent - 1
                if indent == 0:
                    # Change direction:
                    indentIncrease = True

            time.sleep(0.02)  # Add a slight pause.
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.


if __name__ == '__main__':
    main()
