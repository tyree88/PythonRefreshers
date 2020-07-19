import random


def quicksort(dataset, first, last):
    # done recurisvely until no partitions are left
    if first < last:
        # calculate the split point
        pivotIndex = partition(dataset, first, last)

        # sort the two partitions
        quicksort(dataset, first, pivotIndex-1)
        quicksort(dataset, pivotIndex+1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotValue = datavalues[first]

    # establish upp and lower indexes
    lower = first+1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # TODO advance the lower index
        while lower <= upper and datavalues[lower] <= pivotValue:
            lower += 1
        # TODO advance the upper index
        while datavalues[upper] >= pivotValue and upper >= lower:
            upper -= 1
        # TODO if the tow indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange hte pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    print(upper)
    return upper


def main():
    data = [x for x in range(3, 30, 3)]

    random.shuffle(data)
    print(data)
    quicksort(data, 0, len(data)-1)
    print(data)


if __name__ == "__main__":
    main()
