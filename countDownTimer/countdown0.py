import time


def main():
    print('\nCountdown Timer.\n')

    # Enter a valid number of seconds to countdown.
    while True:
        response = input('Enter seconds to start countdown:\n> ')
        if not response.isdecimal():
            continue
        else:
            startTime = int(response)
            break

    # Do the countdown
    countDown(startTime)


def countDown(startTime):
    '''This function returns a preceding countdown of input seconds'''
    while startTime:
        # Get minutes and seconds using divmod() function
        minutes, seconds = divmod(startTime, 60)

        timer = f'{minutes:02} : {seconds:02}'
        print(timer)

        time.sleep(1)

        startTime -= 1

    print('\nCOUNTDOWN COMPLETE')


if __name__ == '__main__':
    main()
