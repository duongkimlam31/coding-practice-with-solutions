"""
Problem: Write a function that determines whether a string is a palindrome or not using recursion. f(string) -> boolean
"""

def isPalindrome(string):
    if (len(string) == 0 or len(string) == 1):
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return True and isPalindrome(string[1:-1])

if __name__ == "__main__":
    test1 = "racecar"
    test2 = "hello"
    test3 = "level"
    test4 = "deified"
    test5 = ""
    test6 = "a"
    test7 = "1112"
    print(isPalindrome(test1))
    print(isPalindrome(test2))
    print(isPalindrome(test3))
    print(isPalindrome(test4))
    print(isPalindrome(test5))
    print(isPalindrome(test6))
    print(isPalindrome(test7))
