# The Birthday Problem

## Description

In a room of just 23 people there’s a 50-50 chance of at least two people having the same birthday. In a room of 75 there’s a 99.9% chance of at least two people matching.

This program performs multiple _Monte Carlo_ Experiments to determine the percentage of people sharing the same birthday for various group sizes.

Read More about the Birthday paradox on [Better Explained](https://betterexplained.com/articles/understanding-the-birthday-paradox/), [Facts and History](https://factsandhistory.com/what-is-the-birthday-paradox/), [Brilliant](https://brilliant.org/wiki/birthday-paradox/), and [here](https://www.scientificamerican.com/article/bring-science-home-probability-birthday-paradox/ 'Birthday Paradox as an experiment')


## How it Works
The Birthday Paradox answers the question; <br>
In a set of $n$ randomly selected people, what is the probability that at least two people share the same birthday?
What is the smallest value of $n$ where the probability is at least 50% or 99%?

To make the Maths easier, let's assume that there are only 365 possible birthdays and that every birthday is equally likely.

Now, in a room of 23 people (inlcuding yourself) you compare your birthday with 22 others, then you compare each person's birthday to every other person in the room.
 - This means the first person compares with 22 other people. The second person compares with 21 others. The third person compares with 20 others, until the second last person compares with the other last person.
 - These comparisons among 23 people add up to (22 + 21 + ... + 1) = 253 possible pairs

The probability that person 1 has a unique birthday is $\frac{365}{365}$ since every date is available. For person 2, the probability drops to $\frac{364}{365}$, since one date is taken by person 1. That trend continues until we get to person 23, whose probability of having a unique birthday is $\frac{343}{365}$. We must multiply all 23 separate probabilities to find out the probability of everyone having unique birthdays; that is:
$P(A') = \frac{365}{365} \times \frac{364}{365} \times \frac{363}{365} \times ... \times\frac{343}{365} = 0.491$ 
Where $P(A')$ is the probability that a person has a unique birthday.
The probability that at least two people in a group share a birthday is given by;

$1-P(A') = 1-0.491 = 0.509 = 50.9\%$

- The function `generateBirthdays` generates random n-birthdays using the `random` module and the `datetime`.
    ```python
    for i in range(numberOfBirthdays):
        yearStart = datetime.date(1990, 1, 1)
        numOfDays = datetime.timedelta(random.randint(0, 364))
        randomDate = yearStart + numOfDays
        birthdays.append(randomDate)
    ```

- The function `generateBirthdayMatches` uses nested loops to find birthday matches in the list of randomly generated n-birthdays
    ```python
    for i, birthdayI in enumerate(birthdays):
        for j, birthdayJ in enumerate(birthdays[i + 1:]):
            if birthdayI == birthdayJ:
                return birthdayI
    ```
    
- The program then performs several Monte Carlo Experiments to determine the percentages for groups of different sizes.


## Program Input & Output

When you run `birthdayParadox.py`, the output will look like this:

```
The Birthday Paradox!
In a set of n-randomly selected people, what is the probability that at least two people share the same birthday? What is the smallest value of n where the probability is at least 50% or 99%?

This program performs multiple simulations to determine the percentage of people sharing the same birthday for various group sizes.
    
How many birthdays (max = 100) do you want to generate?
Enter (q)uit to exit program.
> 23

23 Birthdays Randomly Generated;
29 June, 20 December, 2 September, 24 June, 18 August, 15 Janaury, 1 August, 13 December, 7 December, 21 April, 26 April, 7 June, 5 May, 25 Janaury, 17 June, 21 October, 21 March, 25 November, 16 July, 25 June, 27 July, 11 Janaury, 26 November

In this Simulation... No people share the same birthday!

Generating 23 random birthdays 100 000 times...
0 Simulations Completed...
10000 Simulations Completed...
20000 Simulations Completed...
30000 Simulations Completed...
40000 Simulations Completed...
50000 Simulations Completed...
60000 Simulations Completed...
70000 Simulations Completed...
80000 Simulations Completed...
90000 Simulations Completed...
100 000 Simulations Completed.

In the 100 000 simulations of 23 people;
There are 50460 matching birthdays in the group. 
That is, 23 people have a 50.46% chance of having the same birthday in their group.

.
.
.

How many birthdays (max = 100) do you want to generate?
Enter (q)uit to exit program.
> 75

75 Birthdays Randomly Generated;
30 May, 15 Janaury, 12 March, 6 February, 30 Janaury, 28 November, 9 May, 1 Janaury, 30 December, 23 May, 25 May, 2 October, 21 September, 19 November, 1 Janaury, 21 October, 16 October, 22 July, 1 December, 20 July, 25 April, 7 February, 15 March, 1 December, 4 July, 1 July, 22 July, 10 February, 17 May, 28 December, 12 October, 21 June, 22 April, 17 June, 29 May, 1 February, 7 Janaury, 14 May, 29 November, 9 June, 9 September, 4 July, 22 August, 5 October, 19 May, 31 August, 2 November, 26 May, 3 Janaury, 1 August, 31 October, 1 November, 3 September, 25 June, 18 May, 2 May, 7 September, 26 July, 20 April, 5 July, 20 February, 1 June, 24 October, 20 October, 20 April, 31 October, 6 February, 28 Janaury, 23 September, 28 April, 11 June, 18 February, 19 November, 1 October, 7 Janaury

In this Simulation... Multiple people share the birthday 7 Janaury

Generating 75 random birthdays 100 000 times...
0 Simulations Completed...
10000 Simulations Completed...
20000 Simulations Completed...
30000 Simulations Completed...
40000 Simulations Completed...
50000 Simulations Completed...
60000 Simulations Completed...
70000 Simulations Completed...
80000 Simulations Completed...
90000 Simulations Completed...
100 000 Simulations Completed.

In the 100 000 simulations of 75 people;
There are 99971 matching birthdays in the group. 
That is, 75 people have a 99.971% chance of having the same birthday in their group.
```

- Running the program with `numberOfBirthdays` = 23 and 100 000 simulations, the returned probability value is always $\approx 0.5$ indicating about $50\%$ of the time across 100 000 trials, at least two birthdays shared a date in a group of 23 people.

- Running the program with `numberOfBirthdays` = 75 and 100 000 simulations, the returned probability value is always $\approx 0.999$ indicating about $99.9\%$ of the time across 100 000 trials, at least two birthdays shared a date in a group of 75 people.
