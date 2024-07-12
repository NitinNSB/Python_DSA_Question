'''
Leetcode 234. Palindrome Linked List
Note: Not applicable in this problem but as general fact  a palindrome number with even no of digit is 
      divisible by 11.
'''
# Solution 1:- time complexity O(n) and space complexity O(n)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head :
            return False
        my_list = []
        while head:
            my_list.append(head.val)
            head = head.next
        i = 0
        j = len(my_list) - 1
        while i <= j:
            if my_list[i] != my_list[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
        
# Solution 2:- time complexity O(n) and space complexity O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if only one node return True
        if head and not head.next:
            return True
        
        # Find the middle Node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        curr = slow
        before = None
        after = slow
        while after:
            after = curr.next
            curr.next = before
            before = curr
            curr = after 
        
        # NOW compare 1st and second half
        # Here i have to deal with even and odd number of nodes that why use "fast.next"
        fast = head
        while fast.next :
            if fast.val != before.val:
                return False
            fast = fast.next
            before = before.next
        return True
