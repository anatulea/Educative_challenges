'''
Given the head node of a singly linked list and an integer n, rotate the linked list by n.
'''
# MY SOLUTION
def rotate_list(head, n):
  size = 0

  if head is None:
    return head
  temp = head 
 
 # find length of the linked list
  sizehead =  head
  while sizehead is not None:
    size +=1
    sizehead = sizehead.next
  
  # start from head node and find (n - 1)th from last
  for i in range(0, size-n-1):
    temp = temp.next
# 'temp' is pointing to the (n - 1)th from last and nth from last should be the new head after rotation.
  new_head =  temp.next
# We update 'new_head' pointer to start pointing to nth from last 
# 'temp' node should become the last node of linked list. So we set temp's next as NULL
  temp.next = None

# We'll assign new head to temp and iterate over new list such that temp reaches last node of original list
  temp = new_head
  while temp.next is not None:
    temp = temp.next
# Update temp's next to point to old head.
  temp.next = head
  return new_head




# EDUCATIVE SOLUTION
'''
- Find the length of the linked list.

- If n is negative or n is larger than the length of the linked list, adjust this for the number of rotations needed at the tail of the linked list. The adjusted number is always an integer N where 0 <= N < n.

- If the adjusted number of rotations is 0, then just return the head pointer. This means that no rotations were needed.

- Find the nth node from the last node of the linked list. As we already have the length of the linked list, it is simpler. It is basically getting to the node ‘x’ at length ‘n - N’. Next pointer of node previous to this node, i.e., ‘x’ should be updated to point to NULL.

-  Start from ‘x’ and move to the last node of the linked list. Update next pointer of the last node to point to the head node.

- Make ‘x’ as the new head node. ‘x’ is now the head of the linked list after performing n rotations.


'''
def find_length(head):
  length = 0

  while head:
    length += 1
    head = head.next

  return length

def adjust_rotations_needed(n, length):
  # If n is positive then number of rotations performed is from right side
  # and if n is negative then number of rotations performed from left side
  # Let's optimize the number of rotations.
  # Handle case if 'n' is a negative number.
  n = n % length

  if n < 0:
    n = n + length

  return n

def rotate_list(head, n):

  if head is None or n is 0:
    return

  # find length of the linked list
  length = find_length(head)

  # Let's optimize the number of rotations.
  # Handle case if 'n' is a negative number.

  # If n (number of rotations required) is bigger than
  # length of linked list or if n is negative then
  # we need to adjust total number of rotations needed
  n = adjust_rotations_needed(n, length)

  if n == 0:
    return head

  # Find the start of rotated list.
  # If we have 1, 2, 3, 4, 5 where n = 2,
  # 4 is the start of rotated list.
  rotations_count = length - n - 1
  temp = head
  
  while rotations_count > 0:
    rotations_count -= 1
    temp = temp.next

  # After the above loop temp will be pointing
  # to one node prior to rotation point
  new_head = temp.next

  # Set new end of list.
  temp.next = None

  # Iterate to the end of list and 
  # link that to original head.
  temp = new_head
  while temp.next:
    temp = temp.next
  
  temp.next = head

  return new_head

array1 = [1, 2, 3, 4, 5]
list_head = create_linked_list(array1)
print("Original list: ", end="")
display(list_head)

list_head = rotate_list(list_head, 2)
print("List rotated by 2: ", end="")
display(list_head)