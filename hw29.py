'''

Рисовалка фигур

'''

col = int(input('Height: '))


for i in range(col):
    for j in range(1, 2 * col):
        if j == col - i or j == col + i or i == col - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

for i in range(col):
        for j in range(1, 2 * col):
            if col - i <= j <= col + i:
                print('* ', end='')
            else:
                print('  ', end='')
        print()
