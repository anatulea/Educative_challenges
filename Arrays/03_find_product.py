'''
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.
Sample Input #
arr = [1,2,3,4]
Sample Output #
arr = [24,12,8,6]'''

# MY SOLUTION 
def find_product(lst):
    # Write your code here
    result = []
    for i in range(len(lst)):
        new_list = lst[:i]+ lst[i+1:]

        prod = 1
        for x in new_list:
            prod = prod * x
        result.append(prod)
    return result

'''Solution #1: Using a nested loop'''
def find_product1(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i+1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result
print(find_product([1, 2, 3, 4]))

'''
This solution iterates over the list and calculates the product of all the numbers to the right of the current element as on lines 7 and 8. Then it calculates the product of all the elements to the left of the current element line 10. It then multiplies the two products and returns the result line 14.

Time Complexity #
This algorithm is in O(n^2)O(n
​2
​​ ) because the list is iterated over n(n-1)/2n(n−1)/2 times.'''



'''Solution #2: Optimizing the number of multiplications'''
def find_product2(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


'''The algorithm for this solution is to first create a new list with products of all elements to the left of each element as done on lines 52-54. Then multiply each element in that list to the product of all the elements to the right of the list by traversing it in reverse as done on lines 57-59

Time Complexity #
Since this algorithm only traverses over the list twice, it’s in linear time, O(n)O(n).'''