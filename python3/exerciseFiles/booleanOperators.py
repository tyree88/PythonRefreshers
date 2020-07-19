def main():
    a = True
    b = False
    x = ('bear', 'bunny', 'tree', 'sky', 'rain')
    y = 'bear'

    if y is x[0]:
        print('expression is true')
    else:
        print('expression is false')

    print(id(y))
    print(id(x[0]))


if __name__ == "__main__":
    main()
