def main():
    print('\n 12x12 Multiplication Table.\n')

    # horizontal number labels
    print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
    print('--+---------------------------------------------------')

    # Each row
    for n in range(0, 13):
        print(str(n).rjust(2), end='')
        print('|', end='')

        for m in range(0, 13):
            print(str(n*m).rjust(3), end=' ')
        print()


if __name__ == '__main__':
    main()
