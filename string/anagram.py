"""
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other.

Note:-

If the strings are anagrams you have to return True or else return False

|s| represents the length of string s.


Example 1:

Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have same characters with
        same frequency. So, both are anagrams.
Example 2:

Input:a = allergy, b = allergic
Output: NO
Explanation: Characters in both the strings are 
        not same, so they are not anagrams.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isAnagram() which takes the string a and string b as input parameter and check if the two strings are an anagram of each other. The function returns true if the strings are anagram else it returns false.

Expected Time Complexity:O(|a|+|b|).
Expected Auxiliary Space: O(Number of distinct characters).

Constraints:
1 ≤ |a|,|b| ≤ 105
"""


def isAnagram(a,b):
    dic1 = {}
    dic2 = {}
    for i in range(len(a)):
        if a[i] not in dic1:
            dic1[a[i]] = 1
        else:
            dic1[a[i]] += 1
    for i in range(len(b)):
        if b[i] not in dic2:
            dic2[b[i]] = 1
        else:
            dic2[b[i]] += 1
    if (len(dic1) != len(dic2)):
        return False 
    else:
        for k, v in dic1.items():
            if k not in dic2 or dic1[k] != dic2[k]:
                return False
        return True