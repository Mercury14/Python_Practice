x = int(input('Enter an integer: '))
root = 0
pwr = 2
while pwr > 1 and pwr < 7:
    while root**pwr < x:
        root = root + 1
    if root**pwr == x:
        print(str(root) + '**' + str(pwr), '==', str(x))
        break
    else:
        root = 1
        pwr = pwr + 1
else:
    print('no such pair exists')