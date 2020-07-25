"""
Create a program that return the numerican value from roman numerals
this function is O(1) -> constant since there are a finite set of roman numerals.  
"""


def romanToInt(s):
    romanValues = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    i = 0
    total = 0
    print(s)
    while i < len(s):
        # do the substracting sub cases
        if i+1 < len(s) and romanValues[s[i]] < romanValues[s[i+1]]:
            total += romanValues[s[i+1]] - romanValues[s[i]]
            # must add 2 because total added a 2 sub index
            i += 2
        else:
            # add the total value of i and move on
            total += romanValues[s[i]]
            i += 1
    print(f'The output for the the total is {total}')
    return total


def main():
    data = 'MCMXCIV'
    romanToInt(data)


if __name__ == "__main__":
    main()
