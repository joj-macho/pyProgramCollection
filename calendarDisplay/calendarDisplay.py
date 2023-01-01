import datetime

# Calendar day and month constant
MONTHS = ('Janaury', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

def main():
    print('''
Text-based Calendar Maker.
    ''')

    # prompt user for month and year to display
    while True:
        response = input('Enter a Calendar Year:\n> ')
        # year must be decimal, > 0, and contain 4 digits??
        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break
        else:
            print('Enter a valid Calendar Year!')
            continue
    
    while True:
        response = input('Enter a Calendar Month:\n> ')
        if not response.isdecimal():
            continue
        month = int(response)
        if 1 <= month <= 12:
            break
        print('Please enter a valid number representing Calendar Month')

    # Generate Text Calendar and show it
    calendarShow = generateCalendar(year, month)
    print(calendarShow)

def generateCalendar(year, month):
    '''This function takes in the year and month and returns a printable text calendar.'''
    
    calendarText = ''
    # Calendar Title
    calendarText += (' '*34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    # Calendar days of the week
    calendarText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    # Seperate weeks with horizontal rule
    sepWeeks = ('+----------' * 7) + '+\n'
    # blank Rows
    blankRow = ('|          ' * 7) + '|\n'
    # date
    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    # for each week of the month
    while True:
        calendarText += sepWeeks
        dayRow = ''
        for i in range(7):
            dayLabel = str(currentDate.day).rjust(2)
            dayRow += '|' + dayLabel + (' '*8)
            currentDate += datetime.timedelta(days=1)
        dayRow += '|\n'

        calendarText += dayRow
        for i in range(3):
            calendarText += blankRow

        if currentDate.month != month:
            break

    calendarText += sepWeeks
    return calendarText

if __name__ == '__main__':
    main()
    # print(generateCalendar(2022, 10))