def findmaxno (numbers):
    i=1
    arraylen = len(numbers)
    max = numbers[0]
    while (int(i)<arraylen):
        if (max < numbers[i]):
            max=numbers[i]
            i=int(i)+1
        else:
            i=int(i)+1
    return max