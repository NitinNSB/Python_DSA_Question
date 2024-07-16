# GFG: Sorted Array Search

# Solution 1: Space complexity is O(1) and time complexity is O(n) i.e uses linear search

class Solution:
    def searchInSorted(self,arr, N, K):
        for i in range(N):
            if arr[i] == K:
                return 1
        return -1
 
# Solution 2: Space complexity is O(1) and time Complexity is O(log n) i.e Uses Binary search.

class Solution:
    def searchInSorted(self,arr, N, K):
        left = 0
        right = N-1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == K:
                return 1
            elif arr[mid] < K:
                left = mid + 1
            else:
                right = mid - 1
        return -1