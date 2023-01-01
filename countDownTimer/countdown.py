import sys
import time
import sevenSegment


def main():
    print('\nCountDown Timer.\n')

    # Enter a valid number of seconds to countdown.
    while True:
        response = input(
            'Enter seconds to start countdown. Press Ctrl-C to quit:\n> ')
        if not response.isdecimal():
            continue
        else:
            startTime = int(response)
            break

    # Do the Countdown
    countDown(startTime)


def countDown(startTime):
    '''This function returns a preceding countdown using the seven segment display '''

    try:
        while True:
            # print('\n'*50)
            # Get time from secondsLeft
            hours = str(startTime // 3600)
            minutes, seconds = divmod(startTime, 60)

            # Get digit strings from sevenSegment
            hourDigit = sevenSegment.generateSevenSegment(hours, 2)
            hourTopRow, hourMiddleRow, hourBottomRow = hourDigit.splitlines()

            minuteDigit = sevenSegment.generateSevenSegment(minutes, 2)
            minuteTopRow, minuteMiddleRow, minuteBottomRow = minuteDigit.splitlines()

            secDigit = sevenSegment.generateSevenSegment(seconds, 2)
            secTopRow, secMiddleRow, secBottomRow = secDigit.splitlines()

            # Display the digits:
            print(hourTopRow + '     ' + minuteTopRow + '     ' + secTopRow)
            print(hourMiddleRow + '  *  ' +
                  minuteMiddleRow + '  *  ' + secMiddleRow)
            print(hourBottomRow + '  *  ' +
                  minuteBottomRow + '  *  ' + secBottomRow)

            if startTime == 0:
                print()

                print('\nCOUNTDOWN COMPLETE')

                break

            time.sleep(1)  # one-second pause.
            startTime -= 1

    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
