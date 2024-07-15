# leetcode : 283. Move Zeroes

# Solution 1 : with space complexity of O(1) and time complexity of O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        non_zero = -1

        # sarai non zero ko left mai lai aa array kai
        # phalai mann lai ki non zero element hai hi ni so non_zero = -1
        # or mann lai ki phaila zero element index 0 pai hai i.e zero = 0
        # then check kr ki kya jo element tu zero man raha hai non zero toh nahi hai
        # agar vo non zero hai toh , non-zero index ko increment kr dai
        # then ush index mai vo value dal dai
        # of Zero ko bhi increment kr dai
        # basically tu array ko do part mai divide kr raha hai 
        # left mai non-zero and right mai zero
        for i in range(len(nums)):
            if nums[zero] != 0:
                non_zero += 1
                nums[non_zero] = nums[zero]
            zero += 1 
        
        # Fill the remaining positions with zeros
        for i in range(non_zero + 1,len(nums)):
                nums[i] = 0

         