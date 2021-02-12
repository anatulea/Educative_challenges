'''
Problem Statement: #
In the find_nth function, a certain N is specified as an argument. You simply need to return the node which is N spaces away from the None end of the linked list.

Input #
A linked list and a position N.

Output #
The value of the node n positions from the end. Returns -1 if n is out of bounds.

Sample Input #
LinkedList = 22->18->60->78->47->39->99 and n = 3
Sample Output #
47'''

# MY SOLUTION
from LinkedList import LinkedList
from Node import Node

def find_nth(lst, n):
    if lst.length() < n:
        return -1
    curr = lst.head_node
    for i in range(0, lst.length()-n):
        curr= curr.next_element
    return curr.data

# Solution #1: Double Iteration 

def find_nth(lst, n):
    if (lst.is_empty()):
        return -1

    # Find Length of list
    length = lst.length() - 1

    # Find the Node which is at (len - n + 1) position from start
    current_node = lst.get_head()

    position = length - n + 1

    if position < 0 or position > length:
        return -1

    count = 0

    while count is not position:
        current_node = current_node.next_element
        count += 1

    if current_node:
        return current_node.data
    return -1

# Solution #2: Two Pointers
"""
1. Move end_node forward n times, while nth_node stays at the head
2. If end_node becomes None, n was out of bounds of the array. Return -1 to indicate that the node is not found.
3. One end_node is at nth position from the start, move both end_node and nth_node pointers simultaneously.
4. When end_node reaches the end, nth_node is at the Nth position from the end
5. Return the node’s value
This algorithm also works in O(n) time complexity, but it still adopts the policy of one iteration over the whole list. 
We do not need to keep track of the length of the list."""
def find_nth(lst, n):

    if lst.is_empty():
        return -1

    nth_node = lst.get_head()  # This iterator will reach the Nth node
    end_node = lst.get_head()  # This iterator will reach the end of the list

    count = 0
    while count < n:
        if end_node is None:
            return -1
        end_node = end_node.next_element
        count += 1

    while end_node is not None:
        end_node = end_node.next_element
        nth_node = nth_node.next_element

    return nth_node.data