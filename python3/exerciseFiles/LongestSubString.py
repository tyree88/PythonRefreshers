import platform


def main():
    message()
    a, b = 0, 1
    while(b < 1000):
        a, b = b, a+b
        print(a, b)


def message():
    print('this is the python version {}'.format(platform.python_version()))


if __name__ == '__main__':
    main()
