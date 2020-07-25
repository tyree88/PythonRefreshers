def isOneEditDiff(shortS, longT):
    """
    given two strings s and t, determine if they are both edit distance apart
    there are 3 possiblities to satify one edit distance apart
    1. insert a char into s to get t
    2. remove a char from s to get t 
    3. replace a char from s to get t
    Algorthim
    1. if diff len of s and t is greater(>) then 1 -> return false
    2. make sure s is always shorter then t
    3. do logic 
    """
    lenS, lenT = len(shortS), len(longT)
    if lenS > lenT:
        return isOneEditDiff(t, s)
    if lenT - lenS > 1:
        return False
    for i in range(len(longT)):
        if shortS[i] != longT[i]:
            if lenS == lenT:
                return shortS[i+1:] == longT[i+1:]
            else:
                return shortS[i:] == longT[i+1:]
    return lenS+1 == lenT


def main():
    s = 'ab'
    t = 'acb'
    print(isOneEditDiff(s, t))
    nums = [x for x in range(2)]
    print(nums)
    nums2 = [0, 0]
    new = [x * 0 for x in nums]
    print(new)


if __name__ == "__main__":
    main()
