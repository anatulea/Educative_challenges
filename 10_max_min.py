'''
Problem Statement #
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the third index will have second-largest, and so on. In other words, all the odd-numbered indices will have the largest numbers in the list in descending order and the even-numbered indices will have the smallest numbers in ascending order.

Input: #
A sorted list
lst = [1,2,3,4,5]

Output: #
A list with elements stored in max/min form
lst = [5,1,4,2,3]'''
'''
We then iterate through the list starting from the 0th0th index till the middle of the list indexed as lst[length(list)/2]. So if the length of the given list is 10, the iterator variable i on line 4 in our solution would start from 0 and end at 10/2 = 510/2=5. Note that the starting index 0 in the example is inclusive, and the ending index 5 is exclusive. At each iteration, we first append the largest unappended element and then the smallest. So in the first iteration, i = 0 and lst[-(0+1)] = lst[-1] corresponds to the last element of the list, which is also the largest. So the largest element in the list is appended to result first, and then the current or element indexed by i is appended. Next, the second largest and the second smallest are appended and so on until the end of the list.'''
def max_min(lst): #O(n)
    result = []
    for i in range(len(lst)//2):
        result.append(lst[-(i+1)])
        result.append(lst[i])
    print(result) #[7, 1, 6, 2, 5, 3]
    if len(lst) % 2 == 1:
        result.append(lst[len(lst)//2])
    
    print(result) #[7, 1, 6, 2, 5, 3, 4]
    return result

print(max_min([1, 2, 3, 4, 5, 6,7]))

# Solution #2: Using O(1)O(1) Extra Space
'''
This solution uses some math to store two elements at one index. This is achieved from the following line of code,

lst[i] += (lst[maxIdx] % maxElem) * maxElem 
lst[maxIdx] is stored as a multiplier and lst[i] is stored as remainder. For example in the list, [1, 2, 3, 4, 5, 6, 7, 8, 9], the maxElem is 1010 and 9090 is stored at index 00. One we have 9090, we can get the new element 99 using 90/1090/10. Also, we can go back to the original element, 1, using the expression 90%10.

This allows us to swap the numbers in place without using any extra space. To get the final list, we simply divide each element by maxElem as done in the last for loop.
'''
def max_min2(lst): # O(n) time
    # Return empty list for empty list
    if (len(lst) is 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst 


print(max_min2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) #[9, 0, 8, 1, 7, 2, 6, 3, 5, 4]