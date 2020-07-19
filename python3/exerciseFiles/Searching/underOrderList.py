import random
# searching for an item in an unorderList
# this is also reffered to as a Linear Search
# this search has linear time complexity O(n)


def find_item(item, itemList):
    for i in range(0, len(items)):
        if item == itemList[i]:
            return i
    return None


def main():
    data = [x for x in range(3, 30, 3)]
    random.shuffle(data)


if __name__ == "__main__":
    main()
