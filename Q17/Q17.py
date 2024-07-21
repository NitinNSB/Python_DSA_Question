# Leetcode 485: Max Consecutive Ones

# Solution 1: With time complexity O(n) and space complexity O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, prev = 0, 0
        for x in nums:
            if x == 1:
                count += 1
            else:
                if prev < count:
                    prev = count
                count = 0
        if count > prev:
            return count
        else:
            return prev

