import random
import time
import sys
import bext

# Constants
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

TREE_DENSITY = 0.2
GROWTH_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE = 0.5


def main():
    print('\nWelcome to the Forest Fire Simulation. \n')

    # create Forest
    forest = createForest()
    bext.clear()

    while True:
        displayForest(forest)
        # single sim step
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for i in range(forest['width']):
            for k in range(forest['height']):
                if (i, k) in nextForest:
                    # If we've already set nextForest[(i, k)] on a
                    # previous iteration, just do nothing here:
                    continue

                if ((forest[(i, k)] == EMPTY)
                        and (random.random() <= GROWTH_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(i, k)] = TREE
                elif ((forest[(i, k)] == TREE)
                      and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(i, k)] = FIRE
                elif forest[(i, k)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for p in range(-1, 2):
                        for q in range(-1, 2):
                            # Fire spreads to neighboring trees:
                            if forest.get((i + p, k + q)) == TREE:
                                nextForest[(i + p, k + q)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(i, k)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(i, k)] = forest[(i, k)]
        forest = nextForest

        time.sleep(PAUSE)


def createForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for i in range(WIDTH):
        for k in range(HEIGHT):
            if (random.random() * 100) <= TREE_DENSITY:
                forest[(i, k)] = TREE  # Start as a tree.
            else:
                forest[(i, k)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for k in range(forest['height']):
        for i in range(forest['width']):
            if forest[(i, k)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(i, k)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(i, k)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROWTH_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    main()
