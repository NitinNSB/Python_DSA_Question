# LeetCode 148 : Sort the LL

# Solution 1 : with O(n) space and O(n^2) time complexity, it shows time limit exceeded
# but it is logically correct.
class Solution :
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case : zero or 1 Node
        if head is None or head.next is None:
            return head
        
        # General case
        my_list = []
        jump = head
        while jump:
            my_list.append(jump)
            jump = jump.next
        
        # Sorting the list
        for i in range(len(my_list) - 1):
            for j in range(i+1, len(my_list)):
                if my_list[i].val > my_list[j].val:
                    my_list[i], my_list[j] = my_list[j], my_list[i]
        
        # Linking the sorted nodes
        for i in range(len(my_list) - 1):
            my_list[i].next = my_list[i + 1]

        # Adjusting head and last node
        my_list[len(my_list) - 1].next = None
        head = my_list[0]
        return head  


# Solution 2: Space complexity O(n) and time complexity of O(nlog n)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case : zero or 1 Node
        if head is None or head.next is None:
            return head
        
        # General case
        my_list = []
        jump = head
        while jump:
            my_list.append(jump)
            jump = jump.next
        
        # Sorting the list using merge sort
        def merge(list1, list2):
            merged_list = []
            i, j = 0, 0
            while i < len(list1) and j < len(list2):
                if list1[i].val < list2[j].val:
                    merged_list.append(list1[i])
                    i += 1
                else:
                    merged_list.append(list2[j])
                    j += 1
            
            while i < len(list1):
                merged_list.append(list1[i])
                i += 1
            
            while j < len(list2):
                merged_list.append(list2[j])
                j +=1
            
            return merged_list

        def merge_sort(original_list):
            if len(original_list) == 1:
                return original_list
            mid = len(original_list)//2
            left = merge_sort(original_list[:mid])
            right = merge_sort(original_list[mid:])
            return merge(left,right)
        
        my_list = merge_sort(my_list)
        
        
        # Linking the sorted nodes
        for i in range(len(my_list) - 1):
            my_list[i].next = my_list[i + 1]

        # Adjusting head and last node
        my_list[len(my_list) - 1].next = None
        head = my_list[0]
        return head        