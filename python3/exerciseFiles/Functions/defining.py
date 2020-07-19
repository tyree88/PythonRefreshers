def main():
    # parathenese are used for passing parameters
    # we are passing in 5 to the function
    kitten(5)
    x = kitten()
    print(x)  # returns none - all functions return a value - until kitten has a return


def kitten(n):
    print(f'{n} meow')


    # tests for value equality
    # this __name__ is the name of the file
    # when it is imported. however it is NOT imported and using the main file
if __name__ == '__main__':
    main()
