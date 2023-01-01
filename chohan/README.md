# Chohan Game

## Description

Cho-han is a dice game invented in Japan. Two six-sided dice are rolled and players must guess if the sum is even (cho) or odd (han).


## How it Works

- Using the `random` module, two dice are rolled. The player then decides whether the outcome sum of the two dice is even or odd.
    ```python
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            
            while True:
                bet = input('Choose Cho (even) OR Han (odd)...\n> ').lower()
                if bet != 'cho' and bet != 'han':
                    print('Choose Cho or Han!')
                    continue
                else:
                    break
    ```

- Player wins cash money with each correct guess.
    ```python
    if (dice1 + dice2) % 2 == 0:
                winningBet = 'cho'
            else:
                winningBet = 'han'

            playerWin = bet == winningBet
            if playerWin:
                print(f'You Won $ {betAmount}!')
                money += betAmount
            else:
                print(f'You lost $ {betAmount}!')
                money -= betAmount
    ```

## Program Input & Output

When you run `chohan.py`, the output will look like this:


```
Cho-han Game.
A dice game where players must guess if the resulting sum of the dice is even (cho) or odd (han).
    
You have $5000.

Enter you bet amount. Enter (q)uit to exit.
> 2500

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> cho
DICE Results:
        SAN and SAN ,(3 and 3)
You Won $ 2500!
You have $7500.

Enter you bet amount. Enter (q)uit to exit.
> 7500

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> han
DICE Results:
        GO and NI ,(5 and 2)
You Won $ 7500!
You have $15000.

Enter you bet amount. Enter (q)uit to exit.
> 15000

Dice Rolling...

Choose Cho (even) OR Han (odd)...
> han
DICE Results:
        SAN and SAN ,(3 and 3)
You lost $ 15000!
You have ran out of money. Bye Loser!
```