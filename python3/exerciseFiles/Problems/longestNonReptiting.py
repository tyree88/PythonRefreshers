"""
Get the longest string without a character reptiting itself back to back 

!!!!! KNOW THE DIFFERENCE BETWEEN A SUBSEQUENCE AND SUBSTRING !!!!!

EX:ababcbbcba
A: ababc - is the longest but cba is also a substring without back to back repiting
"""


def nonRepiting(data):
    counter = 0
    sub = ''
    longest = {}
    for i in range(len(data)-1):
        if data[i] != data[i+1]:
            counter += 1
            sub += data[i]
        else:
            longest[sub] = counter
            counter = 0
            sub = ''
    print(longest)


def main():
    data = "abacabbacb"
    nonRepiting(data)


if __name__ == "__main__":
    main()
