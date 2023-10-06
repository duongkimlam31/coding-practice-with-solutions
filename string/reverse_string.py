"""
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i

Input:
S = pqr.mno
Output: mno.pqr
Explanation: After reversing the whole
string , the input string becomes
mno.pqr

Your Task:
You dont need to read input or print anything. Complete the function reverseWords() which takes string S as input parameter and returns a string containing the words in reversed order. Each word in the returning string should also be separated by '.' 


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        tmp = S.split(".")
        result = ""
        for i in range(len(tmp)-1, -1, -1):
            result += tmp[i]
            if i != 0:
                result += "."
        return result