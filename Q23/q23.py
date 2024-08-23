# Leetcode 25:  Reverse Nodes in k-Group

# Solution 1 : Time complexity of O(n) and space complexity of O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Count the total number of nodes in the linked list
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        # Step 2: Determine the number of full parts/groups of size k
        parts = count // k

        # Initialize pointers used for reversing the linked list in groups
        curr = head
        prev, next_node, temp, last = None, None, None, None

        # Step 3: Reverse nodes in groups of k
        for i in range(parts):
            # Mark the start of the current group and the end of the previous group
            last = temp
            temp = curr
            
            # Reverse the current group of k nodes
            for _ in range(k):
                next_node = curr.next  # Store the next node
                curr.next = prev  # Reverse the current node's pointer
                prev = curr  # Move the prev pointer one step forward
                curr = next_node  # Move the curr pointer one step forward
            
            # After the first group is reversed, update the head to the new start
            if i == 0:
                head = prev
            
            # Connect the end of the reversed group to the next node
            temp.next = next_node
            
            # Connect the previous group with the current reversed group
            if last:
                last.next = prev
            
            # Reset prev pointer to None for the next group reversal
            prev = None
        
        # Return the new head of the linked list after all reversals
        return head

    
# Solution 2: Not able to understand other solutions