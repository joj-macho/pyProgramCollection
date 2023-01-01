import datetime
import random
import sys

def main():
    print('''
The Birthday Paradox!
In a set of n-randomly selected people, what is the probability that at least two people share the same birthday? What is the smallest value of n where the probability is at least 50% or 99%?

This program performs multiple simulations to determine the percentage of people sharing the same birthday for various group sizes.
    ''')
    MONTHS = ['Janaury', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Prompt the user to enter valid number of birthdays
    while True:
        response = input('How many birthdays (max = 100) do you want to generate?\nEnter (q)uit to exit program.\n> ')
        if response.startswith('q'):
            print('Bye!')
            sys.exit()
        if response.isdecimal() and (0 < int(response) <= 100):
            numberOfBirthdays = int(response)
            break

    # Generate Birthdays; display day and month of birthdays generated
    print(f'\n{numberOfBirthdays} Birthdays Randomly Generated;')
    birthdays = generateBirthdays(numberOfBirthdays) # list of random birthdays
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        birthMonth = MONTHS[birthday.month - 1]
        birthDate = f'{birthday.day} {birthMonth}'
        print(birthDate, end='')
    print('\n')

    # Find matching birthdays
    birthdayMatch = generateBirthdayMatches(birthdays)
    print('In this Simulation... ', end='')
    if birthdayMatch != None:
        birthMonth = MONTHS[birthday.month - 1]
        birthDate = f'{birthday.day} {birthMonth}'
        print(f'Multiple people share the birthday {birthDate}\n')
    else:
        print('No people share the same birthday!\n')

    # Generate 100_000 Simulations
    print(f'Generating {numberOfBirthdays} random birthdays 100 000 times...')
    simulatedBirthdayMatch = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(f'{i} Simulations Completed...')
        birthdays = generateBirthdays(numberOfBirthdays)
        if generateBirthdayMatches(birthdays) != None:      
            simulatedBirthdayMatch += 1

    print('100 000 Simulations Completed.\n')

    probability = round((simulatedBirthdayMatch/100000)*100, 3)
    print(f'In the 100 000 simulations of {numberOfBirthdays} people;\nThere are {simulatedBirthdayMatch} matching birthdays in the group. \nThat is, {numberOfBirthdays} people have a {probability}% chance of having the same birthday in their group.')




def generateBirthdays(numberOfBirthdays):
    '''This function returns a list of randomly generated birthdays using input numberOfBirthdays.'''
    birthdays = []
    # Generate birthdays from the 1-1-1990
    for i in range(numberOfBirthdays):
        yearStart = datetime.date(1990, 1, 1)
        numOfDays = datetime.timedelta(random.randint(0, 364))
        randomDate = yearStart + numOfDays
        birthdays.append(randomDate)

    return birthdays


def generateBirthdayMatches(birthdays):
    '''This function returns the date of a birthday that occurs more than once.'''
    if len(birthdays) == len(set(birthdays)):
        return None
    # Compare birthdays to find matches
    for i, birthdayI in enumerate(birthdays):
        for j, birthdayJ in enumerate(birthdays[i + 1:]):
            if birthdayI == birthdayJ:
                return birthdayI


if __name__ == '__main__':
    main()