# Leetcode 61: Rotate List

# Solution 1: Time complexity of O(n) and space complexity  of O(1).

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If no node or 1 node or given number or roation is zero then return without rotation
        # because no rotation is needed.
        if not head or head.next or k == 0:
            return head
       
        # Finding length of LL
        length_ll = 0
        jump = head
        while jump:
            length_ll += 1
            jump = jump.next
        
        # Finding correct number of rotations
        k = k % length_ll
        if k == 0:
            return head
        
        # Placing slow and fast pointers to their respective positions
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        
        # Making rotation
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head
        head = new_head

        return head


# Solution 2: This involves transforming the list into a circular linked list and then breaking the circle at 
# the appropriate position.
# Step 1 -> Calculate Length: Traverse the list to find its length '𝑛' and keep a reference to the last node.

# Step 2 -> Make Circular: Link the last node's 'next' to the head, forming a circular linked list.

# Step 3 -> Find New Head: Calculate the position of the new head as new_head_position = 𝑛 −(𝑘 % 𝑛). Traverse 
# to the node just before the new head.

# Step 4 -> Break the Circle: Set the next of the node before the new head to None to break the circle, and 
# return the new head as the start of the rotated list.

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Compute the length of the linked list and find the last node
        length_ll = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length_ll += 1

        # Step 2: Make the linked list circular
        last_node.next = head

        # Step 3: Find the new head after rotation
        k = k % length_ll
        steps_to_new_head = length_ll - k
        position_before_new_head = head
        for _ in range(steps_to_new_head - 1):
            position_before_new_head = position_before_new_head.next
        
        # Step 4: Break the circle and set the new head
        new_head = position_before_new_head.next
        position_before_new_head.next = None
        
        return new_head