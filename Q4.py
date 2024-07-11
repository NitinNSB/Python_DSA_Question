# LeetCode: 1752. Check if Array Is Sorted and Rotated
'''
Q: Given an array nums, return true if the array was originally sorted in non-decreasing order,
   then rotated some number of positions (including zero). Otherwise, return false.There may be
   duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that
      A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1: 
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.You can rotate the array by x = 3 
positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2: 
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums
'''
# Solution 1 with time complexity of O(n logn) and space complexity of O(n).

def check(nums: List[int]) -> bool:
    arr = [x for x in nums]
    arr.sort()   # O(n logn)
    
    # Find the point of rotation (disruption point)
    x = 0
    for i in range(len(nums)): # O(n)
        if i+1 < len(nums):
            if nums[i] > nums[i+1]:
                x = i+1
                break

    # Check if sorted array can be obtained by rotating original array from the disruption point
    for i in range(len(nums)):
        if arr[i] != nums[(i+x) % len(arr)]:
            return False
    return True

# Solution 2 with time complexity of O(n) and space complexity of O(1).

def check(self, nums: List[int]) -> bool:
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i+1)%len(nums)]:
            count +=1
        if count > 1:
            return False
    return True