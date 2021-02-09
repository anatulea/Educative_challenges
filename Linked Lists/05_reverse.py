'''
You have to define the reverse function, which takes a singly linked list and produces the exact opposite list, i.e., the links of the output linked list should be reversed.

Input #
A singly linked list.

Output #
The reversed linked list.

Sample Input #
The input linked list object:

LinkedList = 0->1->2->3-4
Sample Output #
The reversed linked list:

LinkedList = 4->3->2->1->0'''

# my solution
from Node import Node
from LinkedList import LinkedList

def reverse(lst):
  
  # check for empty list
  if lst.is_empty():
    return lst
  # check foor list of one node 
  if lst.length() == 1:
    return lst
  # Initialize three pointers prev as NULL, curr as head and next as NULL.
  previous_element = None
  curr_node = lst.head_node

  # Iterate through the linked list. 
  while curr_node is not None: 
    # Before changing next of current, store next node: next = curr->next
    lst.next_element = curr_node.next_element

    #change next of current: curr->next = prev 
    curr_node.next_element= previous_element

    # Move prev and curr one step forward: prev = curr AND curr = next
    previous_element= curr_node
    curr_node= lst.next_element
    
  lst.head_node = previous_element
  return lst

lst = LinkedList()
lst.insert_at_head(6)
lst.insert_at_head(4)
lst.insert_at_head(9)
lst.insert_at_head(10)
lst.print_list()

reverse(lst)
lst.print_list()

# EDUCATIVE SOLUTION
def reverse(lst):
  # To reverse linked, we need to keep track of three things
  previous = None # Maintain track of the previous node
  current = lst.get_head() # The current node
  next = None # The next node in the list

  #Reversal
  while current:
    next = current.next_element
    current.next_element = previous
    previous = current
    current = next

    #Set the last element as the new head node
    lst.head_node = previous
  return lst