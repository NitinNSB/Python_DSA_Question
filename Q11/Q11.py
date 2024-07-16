# Leetcode : 19. Remove Nth Node From End of List

# Solution 1 : O(1) space and O(n) time complexity
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Base Case if their is only one node
        if head.next is None:
            head = None
            return head
        
        no_of_nodes = 0
        jump = head
        while jump:
            no_of_nodes += 1
            jump = jump.next
        
        # Base case: if nodes are greater than 1 and is equal to 'n'
        if no_of_nodes == n:
            head = head.next
            return head
        
        # General Case
        jump = head
        prev = None
        for _ in range(no_of_nodes - n):
            prev = jump
            jump = jump.next
        prev.next = jump.next
        jump.next = None
        return head

# Solution 2: O(1) space and O(n) time complexity , it is a single pass Solution.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head = None
            return head
        
        slow, fast = head, head

        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If fast is None, we need to remove the head
        if fast is None:
            head = head.next
            slow.next = None
            return head
        
        prev = None
        # Move both pointers until fast reaches the end
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from end
        prev.next = slow.next
        slow.next = None
        return head
