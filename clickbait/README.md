# Click-bait Text Generator

## Description

This program has functions for generating different kinds of clickbait titles. Each of them gets random words from STATES, NOUNS, PLACES, WHEN word list.

## How it works


- This program uses the `random.randint()` function to randomy generate click-bait type titles. 
- Each of defined functions return a different kind of clickbait title. Example, the `generateReasonsWhyHeadline()` function gives titles answering the 'why' prompt.
    ```python
    def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)
    ```


## Program Input & Output

When you run the program `clickbaitGenerator.py`, the output will look like this;

```
```