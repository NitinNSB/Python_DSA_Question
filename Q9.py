# Leetcode : 328. Odd Even Linked List

# Solution 1: Space complexity of O(1) and time complexity of O(n)
# Simple Logic lagaya hai yak pointer ko first node mai point kiya, dusrai ko second mai 
# then dono ko ko yak step chor kai jump karaya ,jissai vo odd or even node ko hi point karai


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd_head = head
        even_head = head.next
        slow, fast = head, head.next
        while fast and fast.next:
            slow.next = fast.next
            slow = slow.next
            if slow.next is not None:
                fast.next = slow.next
                fast = fast.next
            else:
                break
        fast.next = None
        slow.next = even_head
        return head
    

# Solution 2 : with O(n) space complexity and O(n) Time Complexity


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_nodes = []
        even_nodes = []
        
        current = head
        index = 1
        
        # Traverse the list and separate nodes into odd and even lists
        while current:
            if index % 2 == 1:
                odd_nodes.append(current)
            else:
                even_nodes.append(current)
            current = current.next
            index += 1
        
        # Connect the odd nodes
        for i in range(len(odd_nodes)):
            if i+1 < len(odd_nodes): 
                odd_nodes[i].next = odd_nodes[i+1]
        
        # Connect the even nodes
        for i in range(len(even_nodes)):
            if i+1 < len(even_nodes): 
                even_nodes[i].next = even_nodes[i+1]

        # Set next pointer of last node, of even nodes to None 
        even_nodes[len(even_nodes)-1].next = None

        # Set next pointer of Last node, of odd nodes, to first node of even nodes 
        odd_nodes[len(odd_nodes)-1].next = even_nodes[0]
        
        return head       