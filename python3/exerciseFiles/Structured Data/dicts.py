def main():
    animals = {'kitten': 'meow', 'dog': 'bark',
               'lion': 'rawrr', 'giraffe': 'I am a giraffe'}
    animals2 = dict(kitten2='meow', dog2='bark', lion2='grrrr')
    for k in animals.keys():
        print(k)
    animals['lion'] = 'lol'
    animals['monkeys'] = 'lmao'
    for v in animals.values():
        print(v)
    print_dict(animals)
    print('found' if 'monkeys' in animals else "nope")
    print_dict(animals2)


def print_dict(d):
    for k, v in d.items():
        print(f'{k}: {v}')


if __name__ == "__main__":
    main()
