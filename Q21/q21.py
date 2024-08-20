# GFG: Add 1 to a Linked List Number

# Solution 1 : Time complexity of O(n) [Two passes] and space complexity of O(1).


'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        if not head:
            return head
        num = 0
        jump = head
        
        while jump:
            num += jump.data
            jump = jump.next
            if jump:
                num *= 10
                
        num += 1
        num = str(num)
        i = 0
        jump = head
        while jump:
            jump.data = int(num[i])
            i += 1
            # This will check if no of digits is more then no of nodes and if yes then add a new node.
            if (i <= len(num)-1) and (jump.next is None):
                jump.next = Node(0)
            jump = jump.next
            
        
        return head
            
            

# Solution 2:  Time complexity of O(n) [Three passes] and space complexity of O(1).

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    
    def reverse(self, head):
        prev = None
        curr, next_node = head, head
        while next_node:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
        
    
    def addOne(self,head):
        #Returns new head of linked List.
        if not head:
            return head
        
        # Reverse the LL
        head = self.reverse(head)
        jump = head
        carry = 1
        
        # Itirate and Add 1
        while jump:
            val = jump.data + carry
            if val == 10:
                jump.data = 0
                carry = 1
            else:
                jump.data = val
                carry = 0
                break
            jump = jump.next
        
        # Reverse If, needed see the rough
        if carry == 0:
            head = self.reverse(head)
        else:
            new_node = Node(carry)
            new_node.next = head
            head = new_node
            
        return head
            
            
