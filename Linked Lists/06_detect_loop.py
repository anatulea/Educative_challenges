'''
You must implement the detect_loop() function which will take a linked list as input and deduce whether or not a loop is present.

Input #
A singly linked list.

Output #
Returns True if the given linked list contains a loop. Otherwise, it returns False

Sample Input #
LinkedList = 7->14->21->7 # Both '7's are the same node. Not duplicates.
Sample Output #
True'''

# My solution
def detect_loop(lst):
    # create a set to store NONE ADDRESSES
    myset = set()

    curr_node = lst.head_node
    while curr_node is not None:
            # If the set has already
            # this node in hashmap it
            # means their is a cycle
            # (Because you we encountering
            # the node second time).
        if curr_node in myset:
            return True

        # If we are seeing the node for
         # the first time, insert it in hash
        myset.add(curr_node)
        
        # move to the next node
        curr_node = curr_node.next_element
    print(myset) # {<Node.Node object at 0x7fb6a3279a20>, <Node.Node object at 0x7fb6a32799e8>}
    return False





# EDUCATIVE SOLUTION 
# TIME O(n)
# SPACE O(1)
from LinkedList import LinkedList
# Floyd's Cycle Finding Algorithm
#   - Traverse linked list using two pointers.
#   - Move one pointer(slow_p) by one and another pointer(fast_p) by two.
#   - If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.
def detect_loop(lst):
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()
    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element  # Moves one node at a time
        twostep = twostep.next_element.next_element  # Skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False

# ----------------------


lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)

# Adding a loop
head = lst.get_head()
node = lst.get_head()

for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop(lst))