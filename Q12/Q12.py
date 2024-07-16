# LeetCode: 2095. Delete the Middle Node of a Linked List

# Solution 1: Space complexity is O(1) and Time complexity is O(n).
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case : if only 1 node ,then it is the middle node, read the Question
        # to know how middle node is found in this question.
        if head.next is None:
            head = None
            return head
    
        
        # General cases
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        slow.next = None
        return head

# Solution 2 : first traverse the LL and find the lenght, then divide the length by 2 
# and take floor value, now iterate for that 'k' value which you calculated, keep track 
# of previous pointer, now same as of above for general case.For Base case i.e one node
# do the same as above solution. This solution is also of same space and time complexity. 