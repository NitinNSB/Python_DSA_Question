# GFG: Union of Two Sorted Arrays

# Solution 1: With O(n + m) space complexity and time complexity of O((n+m)log(n+m)) as it uses sort()
# function.
class Solution:
    def findUnion(self, arr1, arr2, n, m):
        # Combine both arrays into one
        union_arr = arr1 + arr2
        
        # Convert the combined array to a set to remove duplicates
        union_arr = set(union_arr)
        
        # Convert the set back to a list
        union_arr = list(union_arr)
        
        # Sort the list to ensure the union array is in sorted order
        union_arr.sort()
        
        # Return the sorted union array
        return union_arr



# Solution 2: With O(n + m) space complexity and time complexity 
class Solution:
    def findUnion(self,arr1,arr2,n,m):
        merge_arr = []
        i, j = 0, 0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                # first i was thinking to use "not in" but it has O(n) complexity ,and showing time limit exceeded
                # that why i only checked if list is empty or the last added element is same ,if same don't append 
                # it, just increment the index.
                if len(merge_arr) == 0 or merge_arr[-1] != arr1[i]: 
                    merge_arr.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if len(merge_arr) == 0 or merge_arr[-1] != arr2[j]:
                    merge_arr.append(arr2[j])
                j += 1
            else:
                if len(merge_arr) == 0 or merge_arr[-1] != arr2[j]:
                    merge_arr.append(arr2[j])
                i += 1
                j += 1
        while i < n:
            if len(merge_arr) == 0 or merge_arr[-1] != arr1[i]:
                merge_arr.append(arr1[i])
            i += 1
        
        while j < m:
            if len(merge_arr) == 0 or merge_arr[-1] != arr2[j]:
                merge_arr.append(arr2[j])
            j += 1
        
        
        return merge_arr