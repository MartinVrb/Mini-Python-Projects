for row in range(9):
    for col in range(9):
        if (row == 4) \
                or (row - col == 0) \
                or (row + col == 8) \
                or (2 <= row <= 6 and col not in (3, 4, 5)) \
                or (col % 8 == 0):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
