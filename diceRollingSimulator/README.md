# Dice Rolling Simulator

## Description

This program simulates the rolling of n six-sided die. The result is an ASCII text showing the faces of the rolled dice.

## How it works

- The user chooses the number of dice to roll (between 1 and 6).
- The program uses the `random` module to simulate dice-rolling events.
    - Use the `randint()` function to generate pseudo-random integer numbers between 1 and 6 which will be the results of our rolled die.
        ```python
            diceRollResult = [random.randint(1, 6) for _ in range(numOfDice)]
        ```
- Face(s) of dice corresponding to the rolled event are generated and displayed using the `generateDiceFaces()` function on screen using ASCII diagrams. 

## Program Input & Output

When you run `diceRoll.py`, the output will look like this;

```
Dice Rolling Simulator

How many dice do you want to roll (max 6 dice)?
> 2
RESULTS:
+-------+  +-------+
| O   O |  | O     |
|   O   |  |       |
| O   O |  |     O |
+-------+  +-------+
```
```
Dice Rolling Simulator

How many dice do you want to roll (max 6 dice)?
> 4
RESULTS:
+-------+  +-------+  +-------+  +-------+
| O     |  |       |  | O   O |  | O     |
|       |  |   O   |  |   O   |  |   O   |
|     O |  |       |  | O   O |  |     O |
+-------+  +-------+  +-------+  +-------+
```