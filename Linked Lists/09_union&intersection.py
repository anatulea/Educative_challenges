'''
The union function will take two linked lists and return their union.

The intersection function will return all the elements that are common between two linked lists.

Input #
Two linked lists.

Output #
A list containing the union of the two lists.
A list containing the intersection of the two lists.
Sample Input #
list1 = 10->20->80->60
list2 = 15->20->30->60->45
Sample Output #
union = 10->20->80->60->15->30->45
intersection = 20->60'''

# my solution
from LinkedList import LinkedList
from Node import Node

def union(list1, list2):
    if list1.is_empty():
        return list2
    if list2.is_empty():
        return list1
    

    myset= set()
    curr= list1.head_node

    while curr:
        if curr.data not in myset:
            myset.add(curr.data)
        else:
            list1.delete(curr.data)
        curr= curr.next_element
    curr2 = list2.head_node

    while curr2:
        if curr2.data not in myset:
            myset.add(curr2.data)
            list1.insert_at_tail(curr2.data)
        curr2= curr2.next_element

    return list1

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    if list1.is_empty():
        return list2
    if list2.is_empty():
        return list1
    

    myset= set()
    curr= list1.head_node
    while curr:
        if curr.data not in myset:
            myset.add(curr.data)
        curr= curr.next_element
    myset2 = set()    
    curr2= list2.head_node
    while curr2:
        if curr2.data in myset:
            myset2.add(curr2.data)
        curr2= curr2.next_element
    

    curr3= list1.head_node
    while curr3:
        if curr3.data not in myset2:
            list1.delete(curr3.data)
            curr3= curr3.next_element
        else:
            curr3= curr3.next_element

    return list1



# EDUCATIVE SOLUTION 
def union(list1, list2):
    # Return other List if one of them is empty
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1

    start = list1.get_head()

    # Traverse the first list till the tail
    while start.next_element:
        start = start.next_element

    # Link last element of first list to the first element of second list
    start.next_element = list2.get_head()
    list1.remove_duplicates()
    return list1


def intersection(list1, list2):

    result = LinkedList()
    current_node = list1.get_head()

    # Traversing list1 and searching in list2
    # insert in result if the value exists
    while current_node is not None:
        value = current_node.data
        if list2.search(value) is not None:
            result.insert_at_head(value)
        current_node = current_node.next_element

    # Remove duplicates if any
    result.remove_duplicates()
    return result