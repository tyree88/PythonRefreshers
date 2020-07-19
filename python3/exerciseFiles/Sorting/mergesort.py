import random


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset)//2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO recursively break down the arrays
        mergesort(leftarr)
        print(dataset)
        mergesort(rightarr)
        print(dataset)
        # TODO now perform the merging
        i = 0  # index into the left array
        j = 0  # index into the right array
        k = 0  # index into the merged array

        # TODO while both arrays have
        while (i < len(leftarr) and j < len(rightarr)):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[i]
                j += i
            k += 1
        # TODO if left array still has values add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += i
            k += i

        # TODO if right array still has values add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += j
            k += j


def main():
    data = [x*2 for x in range(2, 39, 2)]
    print(data)
    random.shuffle(data)
    mergesort(data)
    print(data)


if __name__ == "__main__":
    main()
