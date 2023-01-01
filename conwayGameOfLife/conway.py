import copy
import random
import sys
import time

# Constants
# Width and height of the cell grid
WIDTH = 79
HEIGHT = 20
# Dead and live cells
ALIVE = 'O'
DEAD = ' '


def main():
    print('Conway\'s Game of Life: Cellular Automata')

    nextCells = {}
    # Dead or alive cells into nextcell
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if random.randint(0, 1) == 0:
                nextCells[(i, j)] = ALIVE
            else:
                nextCells[(i, j)] = DEAD

    while True:
        print('\n'*50)
        cells = copy.deepcopy(nextCells)
        # Cells
        for i in range(HEIGHT):
            for j in range(WIDTH):
                print(cells[(j, i)], end='')
            print()
        print('Press Ctrl-C to quit.')

        # The next cells step
        for i in range(WIDTH):
            for j in range(HEIGHT):
                # Get the neighboring coordinates of (x, y)
                left = (i - 1) % WIDTH
                right = (i + 1) % WIDTH
                above = (j - 1) % HEIGHT
                below = (j + 1) % HEIGHT

                # Count the number of living neighbors:
                numNeighbors = 0
                if cells[(left, above)] == ALIVE:
                    numNeighbors += 1  # Top-left neighbor is alive.
                if cells[(i, above)] == ALIVE:
                    numNeighbors += 1  # Top neighbor is alive.
                if cells[(right, above)] == ALIVE:
                    numNeighbors += 1  # Top-right neighbor is alive.
                if cells[(left, j)] == ALIVE:
                    numNeighbors += 1  # Left neighbor is alive.
                if cells[(right, j)] == ALIVE:
                    numNeighbors += 1  # Right neighbor is alive.
                if cells[(left, below)] == ALIVE:
                    numNeighbors += 1  # Bottom-left neighbor is alive.
                if cells[(i, below)] == ALIVE:
                    numNeighbors += 1  # Bottom neighbor is alive.
                if cells[(right, below)] == ALIVE:
                    numNeighbors += 1  # Bottom-right neighbor is alive.

                # Set cell based on Conway's Game of Life rules:
                if cells[(i, j)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive:
                    nextCells[(i, j)] = ALIVE
                elif cells[(i, j)] == DEAD and numNeighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    nextCells[(i, j)] = ALIVE
                else:
                    # Everything else dies or stays dead:
                    nextCells[(i, j)] = DEAD

        try:
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    main()
