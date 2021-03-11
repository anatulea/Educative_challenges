'''Given the head pointers of two linked lists where each linked list represents an integer number (each node is a digit), add them and return the resulting linked list. Here, the first node in a list represents the least significant digit.'''
def add_integers(integer1, integer2):
    result = None #final list of added integers
    last = None
    carry = 0 

    while (integer1 or integer2 or carry > 0):
        first = (0 if integer1 is None else integer1.data) # get the value of head node of first list
        second =(0 if integer2 is None else integer2.data) # get the value of the head node for the second list

        sum_val = first + second + carry

        new_sum_node = LinkedListNode(sum_val%10) # create a new linked list node with the value of the mod sum
        carry = sum_val // 10 # add new carry value

        # is the result linked list is empty set it equal to the created node(new_sum_node)
        if  result is None:
            result = new_sum_node
        else:
            # add the new created node as the next of the last node
            last.next = new_sum_node
        last = new_sum_node

        # move to the next nodes in the integer lists 
        if integer1:
            integer1 = integer1.next
        if integer2:
            integer2 = integer2.next
        
    return result