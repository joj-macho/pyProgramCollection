# Pico Fermi Bagels Game

## Description

<p>Pico-Fermi-Bagels is a game where the player must guess a secret three-digit number based on clues. After each guess of the player, the computer answers <strong>fermi</strong> (one digit is at the right position), <strong>pico</strong> (one digit is in the code but on a different position), or <strong>bagels</strong> (none of the digits are correct). The goal is to guess the number in as few tries as possible, so players must use the answers to infer the right code. In this game, players will be given 10 tries to guess the secret number.</p>

## How it Works

- This program uses the in-built `random` module to generate a 3-digit (or `NUM_DIGIT`-digit) secret number.
   ```python
   def generateSecretNumber():
      '''This function returns a string of random 3-digit numbers generated randomly.'''
      n = 3
      return ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])
   ```
- On each guess, clues given by words 'pico', 'fermi', and 'bagels' will be displayed on the screen depending on the guess.
   - Pico if one digit is correct, but in the wrong posistion.
   - Fermi if one digit is correct and in the right position.
   - Bagels if no digit is correct.

      ```python
      for i in range(len(guess)):
         if guess[i] == secretNumber[i]:
               clues.append('Fermi')
         elif guess[i] in secretNumber:
               clues.append('Pico')
      if len(clues) == 0:
         return 'Bagels'
      ```


## Program Input & Output

When you run `picoFermiBagels.py`, the output will look like this:

```
Pico Fermi Bagels!
Can you guess the 3-digit number...?

Here are the clues:
Pico -- One digit is correct, but in the wrong position.
Fermi --- One digit is correct, and in the right position.
Bagels --- No digit is correct.
    
105

I thought of a 3-digit number. Can you guess it?
You have 10 tries to guess the number correctly!

Enter a valid 3-digit number.
Guess #1:
> 012
Pico Pico
Enter a valid 3-digit number.
Guess #2:
> 013
Pico Pico
Enter a valid 3-digit number.
Guess #3:
> 014
Pico Pico
Enter a valid 3-digit number.
Guess #4:
> o15
Enter a valid 3-digit number.
Guess #4:
> 015
Fermi Pico Pico
Enter a valid 3-digit number.
Guess #5:
> 051
Pico Pico Pico
Enter a valid 3-digit number.
Guess #6:
> 510
Pico Pico Pico
Enter a valid 3-digit number.
Guess #7:
> 105
You guessed CORRECTLY!
Do want to Play Again? Enter (y)es or (n)o.
> n
```