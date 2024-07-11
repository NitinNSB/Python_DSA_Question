# GFG : Find length of Loop
'''
Given a linked list of size N. The task is to complete the function countNodesinLoop() that
checks whether a given Linked List contains a loop or not and if the loop is present then 
return the count of nodes in a loop or else return 0. C is the position of the node to which
the last node is connected. If it is 0 then no loop.
'''

# Solution 1:-
def countNodesinLoop(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return 0
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    count = 0
    while slow:
        slow = slow.next
        count += 1
        if slow == fast:
           return count