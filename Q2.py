'''
Q: Given an array arr, return the second largest distinct element from an array. If the second
largest element doesn't exist then return -1.

Example 1:
Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Example 2:
Input: arr = [10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not 
exist so answer is -1.

'''

# Solution 1

def print2largest(arr):
    if len(arr) < 2:
        return -1
    largest = max(arr)
    second_largest = -1
    for x in arr:
        if x > second_largest and x < largest:
            second_largest = x
        
    return second_largest 

print(print2largest([4,5,5,5]))

# Solution 2

def print2largest(arr):
    if len(arr) < 2:
        return -1

    largest = second_largest = -1

    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x > second_largest and x < largest:
            second_largest = x

    return second_largest

print(print2largest([4, 5, 5, 5]))


