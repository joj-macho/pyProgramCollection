# Blackjack Card Game

## Description

This program is a simulation of the blackjack card game where players try to get as close to 21 points as possible without going over.

## How it works

- The function `generateCardDeck()` generates all 52 playable cards and shuffles them for randomness.
    - The player and the dealer then each get two cards from the deck.
    ```python
    deck = []
        for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
            for rank in range(2, 11):
                deck.append((str(rank), suit))
            for rank in ('J', 'K', 'Q', 'A'):
                deck.append((rank, suit))

        random.shuffle(deck)
    ```
- The player makes a move, where the function `showHands()` displays the playing cards on screen with and `generateHand()` sums up all the cards for both the player and the dealer.

## Program Input & Output

When you run `blackjack.py`, the output will look like this:

```
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
    
Available Funds: $5000
Enter bet amount between $1 - $5000. Enter (q)uit to exit.
> 200
Your bet is $200

Dealer: ???
 ___  ___ 
|## | |10 |
|###| | ♦ |
|_##| |_10|

Player: 11
 ___  ___ 
|8  ||3  |
| ♠ || ♥ |
|__8||__3|

(h)it,(s)tand,(d)ouble down
> h
You drew a 8 of ♣
Dealer: ???
 ___  ___ 
|## | |10 |
|###| | ♦ |
|_##| |_10|

Player: 19
 ___  ___  ___ 
|8  ||3  ||8  |
| ♠ || ♥ || ♣ |
|__8||__3||__8|

(h)it,(s)tand
> s
Dealer: 20
 ___  ___ 
|Q  ||10 |
| ♥ || ♦ |
|__Q||_10|

Player: 19
 ___  ___  ___ 
|8  ||3  ||8  |
| ♠ || ♥ || ♣ |
|__8||__3||__8|

You lost.
Press Enter to Continue...

Available Funds: $4800
Enter bet amount between $1 - $4800. Enter (q)uit to exit.
> 4000
Your bet is $4000

Dealer: ???
 ___  ___ 
|## | |8  |
|###| | ♥ |
|_##| |__8|

Player: 14
 ___  ___ 
|9  ||5  |
| ♦ || ♠ |
|__9||__5|

(h)it,(s)tand,(d)ouble down
> h
You drew a 4 of ♦
Dealer: ???
 ___  ___ 
|## | |8  |
|###| | ♥ |
|_##| |__8|

Player: 18
 ___  ___  ___ 
|9  ||5  ||4  |
| ♦ || ♠ || ♦ |
|__9||__5||__4|

(h)it,(s)tand
> s
Dealer: 18
 ___  ___ 
|Q  ||8  |
| ♦ || ♥ |
|__Q||__8|

Player: 18
 ___  ___  ___ 
|9  ||5  ||4  |
| ♦ || ♠ || ♦ |
|__9||__5||__4|

A tie! The bet is returned to you.
Press Enter to Continue...

Available Funds: $4800
Enter bet amount between $1 - $4800. Enter (q)uit to exit.
> 4800
Your bet is $4800

Dealer: ???
 ___  ___ 
|## | |Q  |
|###| | ♣ |
|_##| |__Q|

Player: 13
 ___  ___ 
|6  ||7  |
| ♣ || ♣ |
|__6||__7|

(h)it,(s)tand
> h
You drew a Q of ♥
Dealer: ???
 ___  ___ 
|## | |Q  |
|###| | ♣ |
|_##| |__Q|

Player: 23
 ___  ___  ___ 
|6  ||7  ||Q  |
| ♣ || ♣ || ♥ |
|__6||__7||__Q|

Dealer: 17
 ___  ___ 
|7  ||Q  |
| ♠ || ♣ |
|__7||__Q|

Player: 23
 ___  ___  ___ 
|6  ||7  ||Q  |
| ♣ || ♣ || ♥ |
|__6||__7||__Q|

You lost.
Press Enter to Continue...

No funds to Continue Game.
Bye!
```