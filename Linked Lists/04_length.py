from Node import Node
from LinkedList import LinkedList


def length(lst):
    # start from the first element
    curr = lst.get_head()
    length = 0

    # Traverse the list and count the number of nodes
    while curr:
        length += 1
        curr = curr.next_element
    return length


lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(1)
lst.insert_at_head(0)
print(length(lst))

# my solution
def length(lst):
    size = 0
    if lst.is_empty():
       return 0
    curr_node = lst.head_node
    while curr_node.next_element is not None:
        curr_node= curr_node.next_element
        size+=1
    size+=1
    return size