import random
import time
import sys

#


def main():
    print('\nFast Draw!\nLet us see if you are the fastest draw in the west. \n\nWhen you see "Draw", you have 0.3 seconds to press Enter. You lose if you press Enter before the word "Draw" appears')
    input('Press Enter To Continue ...')

    while True:
        print('Ready ....')
        time.sleep(random.randint(20, 50) / 10)
        print('DRAW!')
        drawTime = time.time()
        input()
        timeElapsed = time.time() - drawTime

        if timeElapsed < 0.01:
            print('You drew before "DRAW" appeared. You lose!')
        elif timeElapsed > 0.3:
            timeElapsed = round(timeElapsed, 4)
            print(f'You took {timeElapsed} seconds to Draw. Too Slow')
        else:
            timeElapsed = round(timeElapsed, 4)
            print(
                f'You took {timeElapsed} seconds to Draw. \nYou are the fastest draw in the West!')

    response = input(
        'Enter (q)uit to quit, press Enter to Play again.').lower()
    if response == 'q' or response == 'quit':
        sys.exit()


if __name__ == '__main__':
    main()
