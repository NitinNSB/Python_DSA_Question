# 160. Intersection of Two Linked Lists
# Solution 1: 
'''Time complexcity of O(n*time complexity of hashing + m*time complexity of hashing) and 
   space complexity of O(n)'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        my_set = set()
        jump = headA
        while jump:             # O(n)
            my_set.add(jump)    # Here add function stores data using hasing
            jump = jump.next
        jump = headB
        while jump:             # O(m)
            if jump in my_set:  # Hasing is used to check membership
                return jump
            jump = jump.next
        return None
    


# Solution 2 : Time Complexity of O(n+m) and space complexity of O(1)
def common_node(List1, List2, d): # Helper Function
    for _ in range(d):
        List1 = List1.next
    while List1 != List2:
        List1 = List1.next
        List2 = List2.next
    return List1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        jump1, jump2 = headA, headB
        l1, l2 = 0, 0
        while jump1:
            l1 += 1
            jump1 = jump1.next
        while jump2:
            l2 += 1
            jump2 = jump2.next
        if l1 > l2:
            return common_node(headA, headB, l1-l2)
        else:
            return common_node(headB,headA, l2-l1)
        


# Solution 3 : Time complexity of O(n+m) and Space complexity of O(1).
# Iska intution thora alag hai yak bar net mai dekh laina
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1