'''
We need to insert a new object at the end of the linked list. You can naturally guess, that this newly added node will point to None as it is at the tail.

Input #
A linked list and an integer value.

Output #
The updated linked list with the value inserted.

Sample Input #
Linked List = 0->1->2
integer = 3
Sample Output #
Linked List = 0->1->2->3
'''
class Node:
    def __init__(self, data):
        self.data=data
        self.next_element = None
    
class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        if (self.head_node is None):
            return True
        else:
            return False
    
    def print_list(self):
        if(self.is_empty()):
            print("List is empty!")
            return False
        
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=' ->')
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

def insert_at_tail(lst, value):
    # Create a new node
    new_node = Node(value)

    # Check if the list is empty, if it is simply point head to new node
    if (lst.is_empty()):
        lst.head_node = new_node
        return

    # If list is not empty, traverse the list to the last node
    temp = lst.get_head()

    while temp.next_element:
        temp = temp.next_element
    
    #Set the next element of the previous node to new node
    temp.next_element = new_node
    return

lst=LinkedList()
lst.print_list() # List is empty!
insert_at_tail(lst, 0)
lst.print_list() # 0 -> None
insert_at_tail(lst, 1)
lst.print_list() # 0 ->1 -> None
insert_at_tail(lst, 2)
lst.print_list() # 0 ->1 ->2 -> None
insert_at_tail(lst, 3)
lst.print_list() # 0 ->1 ->2 ->3 -> None