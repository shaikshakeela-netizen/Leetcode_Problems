"""
Problem: Plus One
LeetCode_Number: 66

Problem Understanding:
You are given an integer represented as an array `digits`,
where each element is a digit (0–9), and the digits are 
stored from most significant to least significant.

Task:
Add 1 to the number and return the resulting array.

Example:
Input:  [1,2,3] → Output: [1,2,4]
Input:  [4,3,2,1] → Output: [4,3,2,2]
Input:  [9,9,9] → Output: [1,0,0,0]

-----------------------------------------------------
💡 Approach: Carry Propagation (Right to Left)

Idea:
1. Start from the last digit (least significant)
2. If digit < 9:
      → Add 1 and return (no carry needed)
3. If digit == 9:
      → Set it to 0 (carry forward)
4. If all digits are 9:
      → Add new leading 1

-----------------------------------------------------
⏱ Time Complexity: O(n)
📦 Space Complexity: O(1) (in-place)

-----------------------------------------------------
🚀 Key Insight:
Only digits with value 9 create a carry.
Stop early when no carry is needed.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        n = len(digits)
        # Traverse from last digit to first
        for i in range(n - 1, -1, -1):
            # Case 1: If digit is less than 9 → just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Case 2: If digit is 9 → set to 0 and carry continues
            digits[i] = 0
        # Case 3: If all digits were 9 → add leading 1
        return [1] + digits


# -------------------------
#  Example Test Cases
# -------------------------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9, 9, 9],
        [9]
    ]
    for digits in test_cases:
        result = solution.plusOne(digits.copy())
        print(f"Input: {digits}")
        print(f"Output: {result}\n")


"""
Expected Output:

Input: [1, 2, 3]
Output: [1, 2, 4]

Input: [4, 3, 2, 1]
Output: [4, 3, 2, 2]

Input: [9, 9, 9]
Output: [1, 0, 0, 0]

Input: [9]
Output: [1, 0]
"""
