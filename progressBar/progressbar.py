import random
import time

BAR = chr(9608)


def main():
    print('\nProgress Bar Simulation.')
    downloaded = 0
    downloadSize = 4096

    while downloaded < downloadSize:
        # Download speed
        downloaded += random.randint(10, 1000)
        # Progress bar
        barString = generateProgressBar(downloaded, downloadSize)

        print(barString, end='', flush=True)

        time.sleep(0.2)

        # Backspaces
        print('\b'*len(barString), end='', flush=True)


def generateProgressBar(progress, total, barWidth=40):
    '''This function returns a string representing a progress bar with barWidth bars and total amount'''

    progressBar = ''
    progressBar += '['

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberOfBars = int((progress/total)*barWidth)
    progressBar += BAR * numberOfBars
    progressBar += ' '*(barWidth - numberOfBars)
    progressBar += ']'

    # Percentage completed
    completed = round(progress/total * 100, 1)
    progressBar += ' ' + str(completed) + '%'
    # Add the numbers:
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar  # Return the progress bar string.


if __name__ == '__main__':
    main()
