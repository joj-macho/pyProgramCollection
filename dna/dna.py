import random
import sys
import time

# DNA Strand
STRAND = [

    '         ##',  # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # Index 9 has no {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']


def main():
    print('\nDNA Animation\n')

    try:
        input('Press Enter To Continue...')

        strandIndex = 0
        while True:
            # Row increment
            strandIndex += 1
            if strandIndex == len(STRAND):
                strandIndex = 0
            # Indexes 0 and 9 have no nucleotides
            if strandIndex == 0 or strandIndex == 9:
                print(STRAND[strandIndex])
                continue

            # Random Nucleotide pairs
            randomSelect = random.randint(1, 4)
            if randomSelect == 1:
                leftNucleotide, rightNucleotide = 'A', 'T'
            elif randomSelect == 2:
                leftNucleotide, rightNucleotide = 'T', 'A'
            elif randomSelect == 3:
                leftNucleotide, rightNucleotide = 'C', 'G'
            elif randomSelect == 4:
                leftNucleotide, rightNucleotide = 'G', 'C'

            # Rows
            print(STRAND[strandIndex].format(leftNucleotide, rightNucleotide))
            time.sleep(0.15)

    except KeyboardInterrupt:
        print('Goodbye')
        sys.exit()


if __name__ == '__main__':
    main()
