'''
You have to implement the find_mid() function which will take a linked list as an input and return the value of the middle node. If the length of the list is even, the middle value will occur at \frac{length}{2}
​2
​
​length
​​ . For a list of odd length, the middle value will be \frac{length}{2}+1
​2
​
​length
​​ +1.

Input #
A singly linked list.

Output #
The integer value of the middle node.

Sample Input #
LinkedList = 7->14->10->21
Sample Output #
14
'''
# BRUTE FORCE 
def find_mid(lst):
    if lst.is_empty():
        return None

    node = lst.get_head()
    mid = 0
    if lst.length() % 2 == 0:
        mid = lst.length()//2
    else:
        mid = lst.length()//2 + 1
        
    # we iterate till the middle index and return the value of that node
    for i in range(mid - 1):
        node = node.next_element

    return node.data
    '''
    This is the simplest way to go about this problem. We traverse the whole list to find its length.
    The middle position can be calculated by halving the length.

    Note: For odd lengths, the middle value would be, mid = length/2 + 1
    Then, we iterate till the middle index and return the value of that node.
    '''

#2: Two Pointers 
def find_mid(lst):
  if lst.is_empty():
    return -1
  current_node = lst.get_head()
  if current_node.next_element == None:
		#Only 1 element exist in array so return its value.
    return current_node.data
  
  mid_node = current_node
  current_node = current_node.next_element.next_element
  #Move mid_node (Slower) one step at a time
  #Move current_node (Faster) two steps at a time
  #When current_node reaches at end, mid_node will be at the middle of List 
  while current_node:
    mid_node = mid_node.next_element
    current_node = current_node.next_element
    if current_node:
      current_node = current_node.next_element
  if mid_node:
    return mid_node.data
  return -1





















# my solution 
def find_mid(lst):
    size1 = (lst.length()/2)
    size2 = (lst.length()//2)
    size = 0
    curr_node =  lst.head_node

    if (lst.length()/2)%2 == 0:
        while curr_node:
            size +=1
            if size == size1:
                return curr_node.data
            curr_node = curr_node.next_element
            
    else:
         while curr_node:
            size +=1
            curr_node = curr_node.next_element
            if size == size2:
                return curr_node.data
            