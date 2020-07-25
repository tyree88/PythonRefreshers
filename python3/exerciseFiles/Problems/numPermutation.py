def numPermutation(nums):
    """
    Get the numbers in the list and find every permutation of the order
    The order will start sorted
    then the permutation will begin with trying to exhaust all of the possibilities
    1. start with the possibilities [1,2,3] -> 1 is removed from the decision space. 
        - remove 3 and 2 from the permutation. Backtrack -> look for the next item within the decision tree 
    2. find the next order -> [1,3,2] this now exhausts all the posibilities in the 1 decision space
    3. to find the next permutation you find the next highest value of 1 == 2 and swap -> [2,3,1] 
    -> this would be the last permutation for 2 so you reverse and start from the beginning
    -> this perm swap can be noticed when a decreasing list is found in a sub list
    Accomplist this by creating pointers at i and j -> i will be the permutation starter and j will be the looker
    """
    # >right
    pi = len(nums) - 1
    # continue moving the pointer if the pointer after is higher
    while pi - 1 >= 0 and nums[pi-1] >= nums[pi]:
        pi += 1
    # >left
    if pi-1 >= 0:  # base case
        pj = pi  # create the second pointer
        print(f'point i is {pi} \n pointer j is{pj}')
        while pj < len(nums) and nums[pj] > nums[pi-1]:  # do the permutations
            pj += 1
            print(f'pointer j is:{pj}')
        # swap the min and max number out of the pointer -> will start the reverse and permutation
        nums[pi-1], nums[pj-1] = nums[pj-1], nums[pi-1]
    ci = pi
    cj = len(nums)-1
    while ci < cj:
        nums[ci], nums[cj] = nums[cj], nums[ci]
        ci += 1
        cj -= 1  # keep the index in range
        print(f'copy pointer i is:{ci}, copy pointer j is:{cj}')


def main():
    data = [x for x in range(3)]
    numPermutation(data)


if __name__ == "__main__":
    main()
