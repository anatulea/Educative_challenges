class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True




############################################
#                                          #
#                 SEARCH                   #
#                                          #
############################################
def search(lst, value):
    if lst.is_empty():
        return False
    
    if value == lst.head_node.data:
        return True
    
    else:
        curr_node = lst.head_node
        while curr_node.next_element is not None:
            if curr_node.next_element.data == value:
                return True
            else:
                curr_node = curr_node.next_element
    return False


lst=LinkedList()
lst.print_list() # List is empty!
lst.insert_at_tail(0)
lst.print_list() # 0 -> None
lst.insert_at_tail(1)
lst.print_list() # 0 ->1 -> None
lst.insert_at_tail(2)
lst.print_list() # 0 ->1 ->2 -> None
lst.insert_at_tail(3)
lst.print_list()
print(search(lst, 3)) # true
print(search(lst, 35)) # False