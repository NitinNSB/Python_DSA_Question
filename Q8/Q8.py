# Leetcode 189. Rotate Array

# Solution 1 : Space and time complexity O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_arr = [x for x in nums]
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = new_arr[i]


# Solution 2 : Time complexity O(n) and space complexity O(1)
class Solution:
    @staticmethod
    def reverse(arr,left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        Solution.reverse(nums,0,len(nums)-1)
        Solution.reverse(nums,0,k-1)
        Solution.reverse(nums,k,len(nums)-1)


#Solution 3 : But it exceed time limits but good for small arrays:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp, j, val = 0, 0, nums[0]
        while j < k:
            for i  in range(len(nums)):
                if i+1 < len(nums):
                    temp = nums[i+1]
                nums[(i+1)%len(nums)] = val
                if i+1 <len(nums):
                    val = temp
            j += 1 
