 
'''
LEETCODE : 142

Q : Given the head of a linked list, return the node where the cycle begins. If there is no 
    cycle, return null.
    There is a cycle in a linked list if there is some node in the list that can be reached again 
    by continuously following the next pointer. Internally, pos is used to denote the index of the 
    node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note 
    that pos is not passed as a parameter.

    NOTE : Do not modify the linked list.
'''

# Solution 1:

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]: 
    my_set = set()
    while head:
        if head  in my_set:
            return head
        else:
            my_set.add(head) 
            head = head.next
    return None 

# Solution 2:
def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]: 
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow 