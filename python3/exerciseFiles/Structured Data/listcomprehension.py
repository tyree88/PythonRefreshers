def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]  # every item in seq * 2
    seq3 = [x for x in seq if x % 3 != 0]  # only elements division by 3
    seq4 = [(x, x**2) for x in seq]  # creates a list of tuples
    from math import pi
    # can call a function . this gets every number in seq and round it to the placement of i
    seq5 = [round(pi, i) for i in seq]
    # create a diction. keys are elements in seq and values are its square value
    seq6 = {x: x**2 for x in seq}
    # create a set seq
    seq7 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6)

    print_list(seq7)


def print_list(sq):
    for i in sq:
        print(i, end=' ')
    print()


if __name__ == "__main__":
    main()
