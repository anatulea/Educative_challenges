'''
Given the head nodes of two linked lists that may or may not intersect, find out if they do in fact intersect and return the point of intersection. Return null otherwise.

In the below example, neither lists intersect. intersect() should return NULL.
head2 -> 13 -> 4 -> Null
head1 -> 29 -> 23 -> 82 -> 11 -> 12 -> 27 -> Null

After adding nodes 12 and 27 in linked list head2, the list now have two same nodes as the linked list head1.
head2 -> 13 -> 4 -> 12 -> 27 ->Null
head1 -> 29 -> 23 -> 82 -> 11 ->  12 -> 27 -> Null

However, in the below example, both lists intersect at the node with data 12, so the node 4 in linked list head2 points 
to node 12 and the node 11 in linked list head1 points to node 12 (have same address).
head2 -> 13 -------> 4 --------->
                                   12 -> 27 -> Null   
head1 -> 29 -> 23 -> 82 -> 11 --->  

'''
def intersect(head1, head2):
  list1node = None
  list1length = get_length(head1)
  list2node = None
  list2length = get_length(head2)

  length_difference = 0
  if list1length >= list2length :
    length_difference = list1length - list2length
    list1node = head1
    list2node = head2
  else:
    length_difference = list2length - list1length
    list1node = head2
    list2node = head1

  while length_difference > 0:
    list1node = list1node.next
    length_difference-=1

  while list1node:
    if list1node is list2node:
      return list1node

    list1node = list1node.next
    list2node = list2node.next
  return None

def get_length(head):
  list_length = 0
  while head:
    head = head.next
    list_length+=1
  return list_length

list_head_1 = create_linked_list([13,4])
list_head_2 = create_linked_list([29,23,82,11])
node1 = LinkedListNode(12)
node2 = LinkedListNode(27)

insert_at_tail(list_head_1, node1)
insert_at_tail(list_head_1, node2)

insert_at_tail(list_head_2, node1)

print("List 1: ", end="")
display(list_head_1)
print("List 2: ", end="")
display(list_head_2)

intersect_node = intersect(list_head_1, list_head_2)
print("Intersect at " + str(intersect_node.data))