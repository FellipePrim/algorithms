
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def array_info (a):

    highest = max(a)
    lowest = min(a)
    total_sum = sum(a)
    average = sum(a) / len(a)

    print(f'The highest number in the array is: {highest}')
    print(f'The lowest number in the array is: {lowest}')
    print(f'The summary of all numbers in the array is: {total_sum}')
    print(f'The average of the array is: {average}')

array_info(a)



