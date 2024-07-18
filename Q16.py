# Leetcode :268. Missing Number

# Solution 1 : Space complexity of O(n) and Time complexity of O(n^2)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_list = list(range(len(nums) + 1))
        for x in my_list:
            if x not in nums:
                return x
        
# Solution 2 : Space complexity of O(1) and Time complexity of O(n^2)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if x not in nums:
                return x
            

# Solution 3 : Space complexity of O(1) and Time complexity of O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2  # Sum of numbers from 0 to n
        return total - sum(nums)
