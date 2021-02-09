class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def print_list(self):

        if self.head is None:
            return False
        
        temp = self.head

        while temp.next_node is not None:
            print(temp.value, end=" ->")
            temp = temp.next_node
        print(temp.value, "-> None")
        return True


#### ------- REMOVE HEAD NODE -------- ####
def remove_head(lst):

    if lst.is_empty():
        print("list is empty")
        return False
    
    if lst.head == lst.tail:
        lst.head = None
        lst.tail = None

    curr_head = lst.head
    new_head = curr_head.next_node
    lst.head = new_head
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
    
    return
   

lst= LinkedList()
lst.print_list() # List is empty
insert_at_head(lst, 3)
lst.print_list() # 3 -> None
insert_at_head(lst, 9)
lst.print_list() # 9 ->3 -> None
insert_at_head(lst, 99) 
lst.print_list() # 99 ->9 ->3 -> None
remove_head(lst)
lst.print_list() # 9 ->3 -> None
remove_head(lst)
lst.print_list() # 3 -> None
remove_head(lst)
lst.print_list() # list is empty
remove_head(lst)
lst.print_list() # list is empty

