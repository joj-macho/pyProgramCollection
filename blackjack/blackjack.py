import random
import sys

# Game Card Character Codes
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

def main():
    print('''
Blackjack Card Game.

This game follows these simple rules:
    - Get as close to 21 without going over to win the game.
    - Kings, Queens, and Jacks are worth 10 points each.
    - Aces are worth 1 or 11 points.
    - Cards 2 through 10 are worth their face value.
    - The bet is returned to the player in case of a tie.
    - The dealer stops hitting at 17.
    - Enter (h)it to take another card.
    - Enter (s)tand to stop taking cards.
    - You can (d)ouble down on your first play to increase your bet + will hit one more time.
    ''')

    money = 5000
    while True:
        # Check if can afford to play
        if money <= 0:
            print('No funds to Continue Game.\nBye!')
            sys.exit()
        print(f'Available Funds: ${money}')
        # Generate bet
        bet = generateBet(money)

        # Player and Dealer Cards: Each gets two cards from the deck
        deck = generateCardDeck()
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        # Player Action
        print(f'Your bet is ${bet}\n')
        while True:
            showHands(playerHand, dealerHand, False)

            if generateHand(playerHand) > 21:
                break

            move = generateMove(playerHand, money - bet)
            if move == 'd':
                additionalBet = generateBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}')
                print(f'Your bet is ${bet}')

            if move in ('h', 'd'):
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}')
                playerHand.append(newCard)

                if generateHand(playerHand) > 21:
                    continue

            if move in ('s', 'd'):
                break

        # Dealer action
        if generateHand(playerHand) <= 21:
            while generateHand(dealerHand) <= 17:
                print('Dealer hits.')
                dealerHand.append(deck.pop())
                showHands(playerHand, dealerHand, False)

                if generateHand(dealerHand) > 21:
                    break
                input('Press Enter to continue.\n\n')

        # Final hand
        showHands(playerHand, dealerHand, True)
        playerVal = generateHand(playerHand)
        dealerVal = generateHand(dealerHand)
        if dealerVal > 21:
            print(f'Dealer busts. You win ${bet}')
            money += bet
        elif playerVal > 21 or playerVal < dealerVal:
            print('You lost.')
            money -= bet
        elif playerVal > dealerVal:
            print(f'You won ${bet}')
            money += bet
        elif playerVal == dealerVal:
            print('A tie! The bet is returned to you.')

        input('Press Enter to Continue...\n')


def generateBet(betAmount):
    '''This function prompts the player for a bet and returns the bet,'''
    while True:
        bet = input(f'Enter bet amount between $1 - ${betAmount}. Enter (q)uit to exit.\n> ').lower()

        if bet.startswith('q'):
            print('Bye!')
            sys.exit()
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= betAmount:
            return bet

def generateCardDeck():
    '''This function returns a list of tuples (rank, suit) for all 52 playing cards.'''
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'K', 'Q', 'A'):
            deck.append((rank, suit))

    random.shuffle(deck)

    return deck

def showHands(playerHand, dealerHand, showDealerHand):
    '''This function shows the player's and dealer's cards'''
    if showDealerHand:
        print('Dealer:', generateHand(dealerHand))
        showCards(dealerHand)
    else:
        print('Dealer: ???')
        showCards(['backside'] + dealerHand[1:])

    # Show player cards
    print('Player:', generateHand(playerHand))
    showCards(playerHand)

def generateHand(cards):
    '''This function adds the cards and returns the value of the cards.'''
    value = 0
    numOfAces = 0

    # Add card values following game rules
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    # Ace card = 1 point or 11 if can be added without exceeding 21
    value += numOfAces
    for i in range(numOfAces):
        if value + 10 <= 21:
            value += 10

    return value
        
def showCards(cards):
    '''This function displays all the cards on hand'''
    rows = ['', '', '', '', '']

    # draw cards
    for i, card in enumerate(cards):
        rows[0] += ' ___ '  # top card line
        if card == 'backside':
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '  # bottom card line
        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} |'  # top rank line
            rows[2] += f'| {suit} |'  # suit line
            rows[3] += f'|_{rank.rjust(2, "_")}|'  # bottom rank line

    # Print each row
    for row in rows:
        print(row)


def generateMove(playerHand, money):
    '''This function asks for player's move and returns 'h' for hit, 's' for stand, and 'd' for double down.'''
    # Player must enter correct move
    while True:
        moves = ['(h)it', '(s)tand']
        # Double down
        if len(playerHand) == 2 and money > 0:
            moves.append('(d)ouble down')

        # Player's move
        move = input(','.join(moves) + '\n> ').lower()
        if move in ('h', 's'):
            return move
        if move == 'd' and '(d)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()