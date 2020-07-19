def main():
    kitten('meow', 'brr', 'grrr')
    dictKitten(Buffy="meow", Zilla="grrr", Gucci="brrr")
    x = dict(Stuffy="meow", Nilla="grrr", Pucci="brrr")
    dictKitten(**x)


def kitten(*args):
    if len(args):  # check len if len is zero then it is False
        for s in args:
            print(s)
    else:
        print('MEOW.')


def dictKitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('dictKitten {} says {}'.format(k, kwargs[k]))
    else:
        print("Meow.")


if __name__ == "__main__":
    main()
