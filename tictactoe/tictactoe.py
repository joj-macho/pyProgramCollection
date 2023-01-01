# Constants
ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '


def main():
    print('\nWelcome to Tic-Tac-Toe.\n')

    gameBoard = generateBlankBoard()
    currentPlayer, nextPlayer = X, 0

    while True:
        print(generateBoardString(gameBoard))
        move = None
        # Ask player for valid move
        while not isValidSpace(gameBoard, move):
            print(f'What is your move {currentPlayer}?')
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)

        #
        if isWinner(gameBoard, currentPlayer):
            print(generateBoardString(gameBoard))
            print(f'{currentPlayer} won the game.')
            break
        elif isBoardFull(gameBoard):
            print(generateBoardString(gameBoard))
            print('The game is a tie.')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer

    print('Bye.')


def generateBlankBoard():
    '''This function generates a blank tic-tac-toe board'''
    board = {}
    print('Empty Board,', board)
    for space in ALL_SPACES:
        # print('space:', space)
        # print('boardspace:', board[space])
        board[space] = BLANK
    print(board)
    return board


def generateBoardString(board):
    '''This function generates a text representation of the board'''
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])


def isValidSpace(board, space):
    '''This function returns True if the space on the board is valid and blank.'''
    return space in ALL_SPACES and board[space] == BLANK


def isWinner(board, player):
    '''This Function returns True if player is the winner.'''
    b, p = board, player
    return ((b['1'] == b['2'] == b['3'] == p) or  # Across top
            (b['4'] == b['5'] == b['6'] == p) or  # Across middle
            (b['7'] == b['8'] == b['9'] == p) or  # Across bottom
            (b['1'] == b['4'] == b['7'] == p) or  # Down left
            (b['2'] == b['5'] == b['8'] == p) or  # Down middle
            (b['3'] == b['6'] == b['9'] == p) or  # Down right
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == p))    # Diagonal


def isBoardFull(board):
    """Return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # If any space is blank, return False.
    return True  # No spaces are blank, so return True.


def updateBoard(board, space, mark):
    """Sets the space on the board to mark."""
    board[space] = mark


if __name__ == '__main__':
    main()
