from decimal import *


def main():
    print(isprime(100))
    a = 8
    b = 9
    x = 'seven then "{1:<03}""{0:>04}"'.format(5, 6)
    # this format is usually used with a variable
    xx = f'seven{a}{b}'
    print('x is {}'.format(xx))
    print(type(x))

    # When dealing with money use the decimal module
    a = Decimal('.10')
    b = Decimal('.30')
    x = a+a+a-b
    print(x) ## this will print 0.00 rather then a long arithmic number


def isprime(n):
    # edge case
    if n <= 1:
        return false
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True


def list_primes():
    for i in range(1000):
        if isprime(i):
            print("prime number{}".format(i))


if __name__ == "__main__":
    main()
