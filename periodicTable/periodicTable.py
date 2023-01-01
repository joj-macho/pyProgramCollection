import csv
import sys
import re


def main():
    print('\nWelcome to the Periodic Table.\n')

    # Read data from csv file
    periodicFile = open('periodic_table/periodictable.csv', encoding='utf-8')
    reader = csv.reader(periodicFile)
    elements = list(reader)
    # print(elements)
    periodicFile.close()

    ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
                   'Group', 'Period', 'Atomic weight', 'Density',
                   'Melting point', 'Boiling point',
                   'Specific heat capacity', 'Electronegativity',
                   'Abundance in earth\'s crust']

    LONGEST_COLUMN = 0
    for key in ALL_COLUMNS:
        if len(key) > LONGEST_COLUMN:
            LONGEST_COLUMN = len(key)

    ELEMENTS = {}
    for line in elements:
        element = {'Atomic Number':  line[0],
                   'Symbol':         line[1],
                   'Element':        line[2],
                   'Origin of name': line[3],
                   'Group':          line[4],
                   'Period':         line[5],
                   'Atomic weight':  line[6] + ' u',  # atomic mass unit
                   'Density':        line[7] + ' g/cm^3',  # grams/cubic cm
                   'Melting point':  line[8] + ' K',  # kelvin
                   'Boiling point':  line[9] + ' K',  # kelvin
                   'Specific heat capacity':      line[10] + ' J/(g*K)',
                   'Electronegativity':           line[11],
                   'Abundance in earth\'s crust': line[12] + ' mg/kg'}

        for key, value in element.items():
            # Remove the [roman numeral] text:
            element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

        # Map the atomic number to the element.
        ELEMENTS[line[0]] = element
        ELEMENTS[line[1]] = element  # Map the symbol to the element.

    while True:
        response = input(
            'Enter symbol or atomic number to examine. Enter (q)uit to exit.\n> ').title()
        if response == 'Q' or response == 'Quit':
            print('Bye.')
            sys.exit()

        if response in ELEMENTS:
            for key in ALL_COLUMNS:
                keyJustified = key.rjust(LONGEST_COLUMN)
                print(keyJustified + ':' + ELEMENTS[response][key])
            input('Press Enter to Continue ...')


if __name__ == '__main__':
    main()
