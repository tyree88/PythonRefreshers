"""
Rotate the given input a given number of input indexs
Clairfing Questions
- Are there constraints on time or space efficiency?
- Should i account for negative inputs?
- What if the rotation input is longer than the list
    A: Continue wrapping 
    A: the rotated "list" would be the same as the original if 'k' is equal to the length
"""


class Node:
    def __init__(self):
        self.head = None
        super().__init__()


# rotate list
# no time/space requirements
# return "rotated" version of input list

def rotate(my_list, num_rotations):
    i = len(my_list) - 1
    counter = 0
    while counter != num_rotations:
        counter += 1
        my_list.insert(0, my_list[i])
        my_list.pop()
    return my_list


def rotateReverse(my_list, num_rotations):
    counter = 0
    while counter != num_rotations:
        counter += 1
        my_list.append(my_list[0])
        del my_list[0]
    return my_list


def main():
    node = Node()
    print(type(node))
    data = [x for x in "hithere"]
    print(data)
    rotate(data, 4)
    rotateReverse(data, 3)


if __name__ == "__main__":
    main()
