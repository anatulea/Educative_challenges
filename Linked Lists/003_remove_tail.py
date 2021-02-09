class Node():
    def __init__(self, value):
        self.value= value
        self.next_node = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def print_list(self):

        if self.is_empty():
            print("List is empty")
            return False
        
        temp  = self.head

        while temp.next_node is not None:
            print(temp.value, end=" ->")
            temp= temp.next_node
        print(temp.value, " -> None")
        return True
    

###     ------   REMOVE TAIL -----    ###
def remove_tail(lst):

    if lst.is_empty():
        print("List is empty")
        return False
    
    if lst.head.next_node is None:
        lst.head = None
        
    else:
        curr_node = lst.head
        prev = curr_node
        while curr_node.next_node != None: #the last element will have next == None
            prev = curr_node
            curr_node = curr_node.next_node
        # At this point, current will be pointing to the last element in the list
        prev.next_node = None
        
    return True



def insert_at_head(lst, value):
    # create a new node
    new_node = Node(value)

    # check if the list is empty, if it is add the node
    if lst.is_empty():
        lst.head= new_node
        lst.next_node = None
    
    # if it is not empty set the current head to be the next node of the new head node
    else:
        new_node.next_node = lst.head
        # set the list head to be the nwe node
        lst.head = new_node
    

lst= LinkedList()
lst.print_list() # List is empty
insert_at_head(lst, 3)
lst.print_list() # 3 -> None
insert_at_head(lst, 9)
lst.print_list() # 9 ->3 -> None
insert_at_head(lst, 99) 
lst.print_list()
remove_tail(lst)
lst.print_list() # 99 ->9  -> None
remove_tail(lst)
lst.print_list() # 99  -> None
remove_tail(lst)
lst.print_list() # List is empty
