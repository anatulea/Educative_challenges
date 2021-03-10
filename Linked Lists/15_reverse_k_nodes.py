'''Given a singly linked list and an integer ‘k’, reverse every ‘k’ element. If k <= 1, then the input list is unchanged. If k >= n (n is the length of the linked list), then reverse the whole linked list.'''

def reverse_k_node(head, k):
    if k<=1 or head is None:
        return head

    reverse = None
    prev_tail = None
    while head and k>0:
        current_head = None
        current_tail = head
        n=k

        while head and n>0:
            temp = head.next
            head.next =current_head
            current_head = head

            head = temp
            n-=1
        if reverse is None:
            reverse = current_head
        if prev_tail:
            prev_tail.next = current_head
        prev_tail = current_tail
    return reverse

'''
1. reversed: it points to the head of the output list.
2. current_head: head of the sub-list of size ‘k’ currently being worked upon.
3. current_tail: tail of the sub-list of size ‘k’ currently being worked upon.
4. prev_tail: tail of the already processed linked list (where sub-lists of size ‘k’ have been reversed).
We’ll work upon one sub-list of size ‘k’ at a time. Once that sub-list is reversed, we have its head and tail in current_head and current_tail respectively. If it was the first sub-list of size ‘k’, its head (i.e., current_head) is the head (i.e., reversed) of the output linked list. We’ll point reversed to current_head of the first sub-list. If it is the 2nd or higher sub-list, we’ll connect the tail of the previous sub-list to head of the current sub-list, i.e., update next pointer of the tail of the previous sub-list with the head pointer of current sub-list to join the two sub-lists.

Let’s apply this algorithm on the following list with 7 elements where k=5.

Initially, all pointers will be null (except head which is pointing to the head of the input linked list.) We’ll reverse the first sub-list of k = 5 nodes. current_head and current_tail will be updated accordingly. We’ll use the head pointer to keep track of the remaining list. As reversed is null after the first sub-list is reversed, so it will be updated with current_head. It will be the head of the final output list. prev_tail will be updated with current_tail. Then, we’ll reverse the next sub-list of size 2 and update current_head and current_tail pointers accordingly. head will become null as there will be no remaining list. We’ll connect the previous tail with the current head in the end.'''

