import sys
import time
import sevenSegment


def main():
    print('\nDigital Timer.\n')

    try:
        while True:
            # First clear the screen
            # print('\n'*50)
            # Get time from computer
            currentTime = time.localtime()
            hours = str(currentTime.tm_hour % 24)
            minutes = str(currentTime.tm_min)
            seconds = str(currentTime.tm_sec)

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

            print()
            print('Press Ctrl-C to quit.')

            # Loop through seconds
            while True:
                time.sleep(0.01)
                if time.localtime().tm_sec != currentTime.tm_sec:
                    break

    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.)


if __name__ == '__main__':
    main()
