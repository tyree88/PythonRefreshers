"""
Palindrome is a string of characters that are the read the forwards and backwards
STEPS to find a planindrome
1. check for a string if none return false
2. get front and last letter. then compare
3. if they == then move down the list 
4. return if false
Questions to ask
- Do we care about case senstive
- what if we wanted to Ignorate punctuation
- do we want to ignore spaces
Edge Cases
- what if we wanted to Ignorate punctuation

"""


def recursivePalindrome(data):
    # recursive way
    if len(data) <= 1:
        return True
    if data[0] != data[-1]:
        return False
    return recursivePalindrome(data[1:-1])


def casePlaindrome(data):
    if isinstance(data, str):
        lower = data.lower()
    else:
        return False
    for i in range(len(data)-1):
        if data[i] != data[-i - 1]:
            return False
    return True


def ignorePunPalindrome(data):
    ignore = ['!', ':', ',', '?', '.', ' ', '@', '#', '$', '%', '^', '&', '*',
              '_', '-', '{', '}', '\ ', '/', ']', '[', "'", '"', ';', '(', ')', '`']
    cleanData = [x for x in data if x not in ignore]
    print(cleanData)
    return (recursivePalindrome(cleanData))


def main():
    data = "r!a.c,ecar!.,?"
    data1 = 'able was I, ere I saw elba'
    # print(recursivePalindrome(data))
    # print(casePlaindrome(data))
    print(ignorePuncPalindrome(data))
    print(ignorePuncPalindrome(data1))


if __name__ == "__main__":
    main()
