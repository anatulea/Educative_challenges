'''
Given a list of size n, can you find the second maximum element in the list? Implement your solution in Python and see if your output matches the correct output!
'''
# Solution #1: Sort and index  O(nlogn)
def find_second_maximum(lst): 
    lst.sort()
    if len(lst) >= 2:
        return lst[-2]
    else:
        return None


print(find_second_maximum([9, 2, 3, 6]))

# Solution #2: Traversing the list twice #O(n)
def find_second_maximum(lst):
    first_max = float('-inf')
    second_max = float('-inf')
    # find first max
    for item in lst:
        if item > first_max:
            first_max = item
    # find max relative to first max
    for item in lst:
        if item != first_max and item > second_max:
            second_max = item
    return second_max


print(find_second_maximum([9, 2, 3, 6]))


# Solution #3: Finding the Second Maximum in one Traversal #O(n)
def find_second_maximum(lst):
   if (len(lst) < 2):
       return
   # initialize the two to infinity
   max_no = second_max_no = float('-inf')
   for i in range(len(lst)):
       # update the max_no max_no if max_no value found
       if (lst[i] > max_no):
           second_max_no = max_no
           max_no = lst[i]
       # check if it is the second_max_no max_no and not equal to max_no
       elif (lst[i] > second_max_no and lst[i] != max_no):
           second_max_no = lst[i]
   if (second_max_no == float('-inf')):
       return
   else:
       return second_max_no


print(find_second_maximum([9, 2, 3, 6]))


