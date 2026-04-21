'''
🧩 LeetCode Problem: Valid Palindrome
📄 Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Leetcode number : 125

Approach (Two Pointer Technique)
Use two pointers:
left starting from the beginning
right starting from the end
Skip non-alphanumeric characters using isalnum()
Convert characters to lowercase before comparing
If mismatch found → return False
If pointers cross without mismatch → return True

👉 This avoids creating a new string and is memory efficient.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


'''
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

'''
