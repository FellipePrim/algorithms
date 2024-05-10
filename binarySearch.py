def binarySearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = list[middle]
        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return None

myList = [1, 3, 5, 7, 9, 12, 15, 18, 21, 24, 27]

print (binarySearch(myList, 18)) # => 7 (position)
print (binarySearch(myList, 15)) # => 6 (position)
print (binarySearch(myList, -1)) # => None

