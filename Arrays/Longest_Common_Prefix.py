""" 
Problem: Longest Common Prefix
Leetcode_Number : 14
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix among given strings

        Parameters:
        strs (List[str]): List of input strings

        Returns:
        str: Longest common prefix
        """
        # Edge case: if list is empty
        if not strs:
            return ""
        # Step 1: Assume first string as prefix
        prefix = strs[0]
        # Step 2: Compare with remaining strings
        for s in strs[1:]:
            # Step 3: Shrink prefix until it matches start of current string
            while not s.startswith(prefix):
                # Remove last character from prefix
                prefix = prefix[:-1]
                # If prefix becomes empty → no common prefix exists
                if prefix == "":
                    return ""
        # Step 4: Return final prefix
        return prefix


# -------------------------
# 🔍 Example Test Cases
# -------------------------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interview", "internet", "internal"]
    ]

    for strs in test_cases:
        result = solution.longestCommonPrefix(strs)
        print(f"Input: {strs}")
        print(f"Longest Common Prefix: '{result}'\n")


"""
Expected Output:

Input: ['flower', 'flow', 'flight']
Longest Common Prefix: 'fl'

Input: ['dog', 'racecar', 'car']
Longest Common Prefix: ''

Input: ['interview', 'internet', 'internal']
Longest Common Prefix: 'inte'
"""
