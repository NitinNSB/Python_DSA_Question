# Leetcode:Add Two Numbers[SLL]

# Solution  1: Time complexity of O(n) and space complexity of O(1)
# In this i have done redundant code .


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse_list(self, head):
        curr = head
        prev, next_node = None, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

     
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        
        # Creating head of resulting LL
        head = ListNode()

        jump_l1, jump_l2, jump_head = l1, l2, head
        carry, data = 0, 0

        while jump_l1 or jump_l2:
            jump_head.next = ListNode() # create a new node
            jump_head = jump_head.next # point to that new node

            if not jump_l1:
                data = jump_l2.val + carry
            elif not jump_l2:
                data = jump_l1.val + carry
            else:
                data = jump_l1.val + jump_l2.val + carry

            if data > 9:
                carry = 1
                jump_head.val = data % 10
            else:
                carry = 0
                jump_head.val = data
            
            if not jump_l1:
                jump_l2 = jump_l2.next
            elif not jump_l2:
                jump_l1 = jump_l1.next
            else:
                jump_l2 = jump_l2.next
                jump_l1 = jump_l1.next
            

        # Now reverse the LL
        head = self.reverse_list(head.next)

        # Now if carry, append a new node with value = carry
        if carry == 1:
            new_node = ListNode(carry)
            new_node.next = head
            head = new_node
        
        return self.reverse_list(head)


 # Solution 2 : Time complexity of O(n) and space complexity O(1)
 # IN this i have removed that redundant code, for exmple reverse_list function 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        jump_l1, jump_l2, jump_head = l1, l2, head
        carry, value = 0, 0

        while jump_l1 or jump_l2:
            if not jump_l1:
                value = jump_l2.val + carry
                jump_l2 = jump_l2.next
            
            elif not jump_l2:
                value = jump_l1.val + carry
                jump_l1 = jump_l1.next
            
            else:
                value = jump_l1.val + jump_l2.val + carry
                jump_l2 = jump_l2.next
                jump_l1 = jump_l1.next
            
            if value > 9:
                carry = 1
                jump_head.next = ListNode(value % 10)
                jump_head = jump_head.next
            
            else:
                carry = 0
                jump_head.next = ListNode(value)
                jump_head = jump_head.next
            
        if carry:
            jump_head.next = ListNode(carry)
        
        return head.next


               