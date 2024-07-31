# Leetcode : 136. Single Number
# Solution 1 : Time complexity O(n) , space complexity O(m) i.e m < n where m = no of values stored in dictionary
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {}
        for x in nums:
            # By default, membership operation on dictionaries check whether the dictionary has a given key or not.
            if x in my_dict:
                my_dict[x] += 1
            else:
                my_dict[x] = 1
        
        for key, val in my_dict.items():
            if val == 1:
                return key
        

# Solution 2: Time complexity O(n) and space complexity O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # Zero isliyai liya Qki 0 ^ any = any
        # So no affect on starting of loop.
        for x in nums:
            result = result ^ x
        return result
        

        
