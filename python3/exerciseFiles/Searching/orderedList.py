import random
# this is also referred to as a binary searc h
# steps is getting the size
# then setting the upper and lower
# then calculate the middle point so know the comparison point


def binarySearch(item, dataset):
    # get the list size
    listSize = len(dataset)-1
    # start at the two ends of the list
    lowerIndex = 0
    upperIndex = listSize

    while lowerIndex <= upperIndex:
        # find the middle point
        middle = upperIndex // 2

        # if item is found, return the index
        if dataset[middle] == item:
            return middle
        # otherwise get the next midpoint
        if item > dataset[middle]:
            lowerIndex = middle + 1
        else:
            upperIndex = middle-1

    if lowerIndex > upperIndex:
        return None


def main():
    data = [x for x in range(5, 10, 3)]
    print(data)
    print(binarySearch(35, data))
    data1 = [x for x in range(1, 8)]
    data2 = [x for x in range(1, 10)]
    print(str(data1)[1:-1])
    print(str(data2)[1:-1])

    data3 = map(add, data1, data2)
    print(data3)


main()
