'''
Given a list, can you rearrange its elements in such a way that the negative elements appear at one end and positive elements appear at the other?
Sample Input #
[10,-1,20,4,5,-9,-6]
Sample Output #
[-1,-9,-6,10,20,4,5]
'''
def rearrange(lst):
    # Write your code here
    return sorted(lst)

# Solution #1: Using Auxiliary Lists #O(n)
def rearrange(lst):
    neg = []
    pos = []
    # make a list of negative and positive numbers
    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
    # merge two lists and return
    return neg + pos


print(rearrange([10, -1, 20, 4, 5, -9, -6]))

# Solution #2: Rearranging in Place #O(n)
def rearrange(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if (lst[curr] < 0):
            # if not the last negative number
            if (curr is not leftMostPosEle):
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst


print(rearrange([10, -1, 20, 4, 5, -9, -6]))


# Solution #3: Pythonic Rearrangement #O(n)
def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

