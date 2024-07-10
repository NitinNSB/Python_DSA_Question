'''
Question : Allen's Value

You are given an array A of 'n' (n ≥ 3) distinct integers. Your friend Allen removes 
only 2 elements from this array, adds a value (x > 0) to all the remaining elements, 
shuffles the array, and leaves the newly formed array G for you.

Your task is to return the minimum possible value that Allen had added to each element 
of array A to get to array G.
Note:

    It is guaranteed that at least one such value which will be greater than 0 will always exist.
    Consider 1-based indexing.

Input Specification:

    input1: An integer value 'n', representing the size of array A.
    input2: An integer array A.
    input3: An integer array G created by Allen.

Output Specification:

    Return the minimum possible value that Allen had added to each element of array A to form array G.
    '''

def minimum_possible(input1, input2, input3):
    input2.sort()
    input3.sort()
    smallest_input3 = input3[0]
    min_possible_value = 1
    for i in range(input1):
        if input2[i] > smallest_input3:
            break
        elif smallest_input3 - input2[i] > 0 :
            min_possible_value = smallest_input3 - input2[i]
    return min_possible_value

input1 = 3
input2 = [2, 4, 6]
input3 = [7]
print(minimum_possible(input1, input2, input3))