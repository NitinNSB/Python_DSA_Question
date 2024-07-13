# Leetcode 26: Remove Duplicates from Sorted Array

# Solution 1: With O(n) space and Time complexity

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_arr = []
        for x in nums:
            if x not in new_arr:
                new_arr.append(x)
        for i in range(len(new_arr)):
            nums[i] = new_arr[i]
        return len(new_arr)

# Solution 2: With O(n) Time and O(1) Space

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        size = len(nums)
        for i in range(size-1):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1