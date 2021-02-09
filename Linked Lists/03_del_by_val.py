class Node():
    def __init__(self, value):
        self.value =  value
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

        if self.head is None:
            print("list is empty")
            return False
        
        curr = self.head

        while curr.next_node is not None:
            print(curr.value, end=" ->")
            curr = curr.next_node
        print(curr.value, " -> None")
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

def del_by_value(lst, target):
    if lst.is_empty():
        print("The list is empty")
        return -1
    curr_node =  lst.head
    if curr_node.value == target:
        lst.head = curr_node.next_node
        if lst.head == None or lst.head.next_node == None:
            lst.tail= lst.head
        return

    while curr_node.next_node is not None and curr_node.next_node.value != target:
        curr_node = curr_node.next_node

    if curr_node.next_node != None:
        curr_node.next_node = curr_node.next_node.next_node
        if curr_node.next_node ==None:
            lst.tail = curr_node
        return
    else:
        print("Target not found")

lst= LinkedList()
lst.print_list() # List is empty
insert_at_head(lst, 3)
lst.print_list() # 3 -> None
insert_at_head(lst, 9)
lst.print_list() # 9 ->3 -> None
insert_at_head(lst, 99) 
lst.print_list()
del_by_value(lst, 4)
lst.print_list() #Target not found
del_by_value(lst, 9)
lst.print_list() #99 ->3  -> None


# My solution in educative
def delete(lst, value):

    if lst.is_empty():
        print("List is empty")
        return False
    
    curr_node =  lst.head_node

    if curr_node.data == value:
        lst.head_node= curr_node.next_element
        return True

    while curr_node.next_element is not None and curr_node.next_element.data != value:
        curr_node =  curr_node.next_element

    if curr_node.next_element != None:
        curr_node.next_element = curr_node.next_element.next_element 
        return True 
    else:
        print("target not found")
        return False



############## educative solutions  #####

# |||||||||||||||||||||||||||||||||||||||||||
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV



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

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

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

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if (first_element is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while(temp is not None):
            if(temp.data is dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None


def delete(lst, value):
    deleted = False
    if lst.is_empty():  # Check if list is empty -> Return False
        print("List is Empty")
        return deleted
    current_node = lst.get_head()  # Get current node
    previous_node = None  # Get previous node
    if current_node.data is value:
        lst.delete_at_head()  # Use the previous function
        deleted = True
        return deleted

    # Traversing/Searching for Node to Delete
    while current_node is not None:
        # Node to delete is found
        if value is current_node.data:
            # previous node now points to next node
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element

    if deleted is False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")

    return deleted


lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 4)
lst.print_list()
