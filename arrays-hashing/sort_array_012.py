"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated into ascending order.

Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated into ascending order.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

def sort012(arr):
        # code here
        count = {0:0, 1:0, 2:0}
        c = 0
        for i in range(len(arr)):
            count[arr[i]] += 1
        for k, v in count.items():
            while v > 0:
                arr[c] = k
                v -= 1
                c+=1
        return arr