
a = [9, 4, 3, 2, 5, 7, 6, 8, 1]

def indexFinder(a):

    b = int(input(f'Select a number from the list: {a} '))

    for i in range(len(a)):
        if b == a[i]:
            print(f'The position of the number you chose is: {i+1}')
            print(f'The index of the number you chose is: {i}')
            break
    else:
        print('Number not found in the list.')

indexFinder(a)