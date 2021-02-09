'''
Given an unsorted list AA, the maximum sum sub list is the sub list (contiguous elements) from AA for which the sum of the elements is maximum. In this challenge, we want to find the sum of the maximum sum sub list. This problem is a tricky one because the list might have negative integers in any position, so we have to cater to those negative integers while choosing the continuous sublist with the largest positive values.'''
def find_max_sum_sublist(lst): 
  if (len(lst) < 1): 
    return 0;

  curr_max = lst[0];
  global_max = lst[0];
  length_array = len(lst);
  for i in range(1, length_array):
    if curr_max < 0: 
      curr_max = lst[i]
    else:
      curr_max += lst[i]
    if global_max < curr_max:
      global_max = curr_max

  return global_max;


lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1];
print("Sum of largest subarray: ", find_max_sum_sublist(lst));


'''The basic idea of Kadane’s algorithm is to scan the entire list and at 
each position find the maximum sum of the sublist ending there. This is achieved 
by keeping a current_max for the current list index and a global_max. 
The algorithm is as follows:'''

# current_max = A[0]
# global_max = A[0]
# for i = 1 -> size of A
#     if current_max is less than 0
#         then current_max = A[i]
#     otherwise 
#         current_max = current_max + A[i]
#     if global_max is less than current_max 
#         then global_max = current_max
'''
Runtime complexity #
The runtime complexity of this solution is linear, O(n)O(n).

Space complexity #
The memory complexity of this solution is constant, O(1)O(1).

Let’s run through an example to understand how it works.
Initially, the current_max and global_max are both set to the value at A[0], that is, -4:'''