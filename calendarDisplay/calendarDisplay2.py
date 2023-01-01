import calendar


def main():
    print('\nCalendar Display\n')

    # Prompt the user to display yearly calendar, or monthly calendar
    while True:
        response = input(
            'Select option to display:\nEnter 1 to show year only.\nEnter 2 to show year and month.\n> ')
        if response in ['1', '2']:
            opt = int(response)
            break
        else:
            print('Enter A Valid Integer Option!!')

    if opt == 1:
        print('Yearly Calendar Display.')
        yearInput = int(input('Enter the Calendar Year to Display.\n> '))
        print(calendar.calendar(yearInput))

    elif opt == 2:
        print('Monthly Calendar Display.')
        yearInput = int(input('Enter the Calendar Year to Display.\n> '))
        monthInput = int(
            input('Enter the Calendar Month (1-12) to Display.\n> '))
        print(calendar.month(yearInput, monthInput))


if __name__ == '__main__':
    main()
