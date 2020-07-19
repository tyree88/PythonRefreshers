import random


def bubbleSort(dataSet):
    # TODO start with the array length and decrement each time
    for i in range(len(dataSet)-1, 0, -1):
        for j in range(i):
            if dataSet[j] > dataSet[j+1]:
                temp = dataSet[j]
                dataSet[j] = dataSet[j+1]
                dataSet[j+1] = temp
        print(f'Current State: {dataSet}')


def main():
    data = [x for x in range(15)]
    random.shuffle(data)
    bubbleSort(data)
    print(f"Result {data}")


if __name__ == "__main__":
    main()
