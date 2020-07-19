def main():
    a = set('were gunna need a bigger boat')
    b = set('im sorry, dave. Im afraid i cant do that')
    print_set(a)
    print_set(b)
    print_set(a - b)  # members in set A but not in set b
    print_set(a ^ b)  # a or B but not Both
    print_set(a | b)  # in one or Both of sets
    print_set(a & b)  # found in both


def print_set(s):
    print('{', end='')
    for x in s:
        print(x, end='')
    print('}')


if __name__ == "__main__":
    main()
