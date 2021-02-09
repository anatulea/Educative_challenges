class Node():
    def __init__(self, val):
        self.val= val
        self.next_node= None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if(self.head is not None):
            return False
        else:
            return True

    def get_head(self):
        return self.head

    def print_list(self):

        if self.is_empty():
            print("List is empty")
            return False
        
        curr_node = self.head

        while curr_node.next_node is not None:
            print(curr_node.val, end=" ->")
            curr_node = curr_node.next_node
        print(curr_node.val, "-> None")
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
