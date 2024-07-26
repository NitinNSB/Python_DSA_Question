# GFG : Sort a linked list of 0s, 1s and 2s

# Solution 1 : Time  complexity of O(n) and space complexity of O(1).one pass solution.
class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None

class Solution:
    def segregate(self, head):
        dummy_zero = Node(0)
        dummy_one = Node(0)
        dummy_two = Node(0)
        point_zero, point_one, point_two = dummy_zero, dummy_one, dummy_two
        jump = head
        
        while jump:
            if jump.data == 0:
                point_zero.next = jump
                point_zero = point_zero.next
            elif jump.data == 1:
                point_one.next = jump
                point_one = point_one.next
            else:
                point_two.next = jump
                point_two = point_two.next
            
            jump = jump.next
        
        # Case-1: When all three exist or only 1 and 2 exist.
        if dummy_zero.next and dummy_one.next:
            point_zero.next = dummy_one.next
            point_one.next = dummy_two.next
            point_two.next = None
            return dummy_zero.next
        
        # Case-2: When 1 and 2 exist or only 1 .
        elif dummy_one.next:
            point_one.next = dummy_two.next
            point_two.next = None
            return dummy_one.next
        
        # Case-3: When only 0 and 2 exist or only 0.
        elif dummy_zero.next:
            point_zero.next = dummy_two.next
            point_two.next = None
            return dummy_zero.next
        
        # Case-4: When only 2 exist:
        elif dummy_two.next:
            point_two.next = None
            return dummy_two.next 
        

# Solution 2: A little improved version of sol-1 with combined cases
class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None

class Solution:
    def segregate(self, head):
        dummy_zero = Node(0)
        dummy_one = Node(0)
        dummy_two = Node(0)
        point_zero, point_one, point_two = dummy_zero, dummy_one, dummy_two
        jump = head
        
        while jump:
            if jump.data == 0:
                point_zero.next = jump
                point_zero = point_zero.next
            elif jump.data == 1:
                point_one.next = jump
                point_one = point_one.next
            else:
                point_two.next = jump
                point_two = point_two.next
            
            jump = jump.next
        
        if dummy_one.next:
            point_zero.next = dummy_one.next
            point_one.next = dummy_two.next
        else:
            point_zero.next = dummy_two.next
        
        if dummy_two.next:
            point_two.next = None
        
        return dummy_zero.next
 
# Solution 3 : Time complexity of O(2n) i.e with 2 passes and space complexity of O(1).
# Take 3 variables and count no of 0's, 1's, 2's by treversing the LL. Now again treverse 
# the LL and replace values of nodes  according to counts of  0's, 1's and 2's in increasing
# order.