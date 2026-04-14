"""
LeetCode Problem: Convert Sorted Array to Binary Search Tree
Number: 108
Approach:
- Use Divide & Conquer
- Pick middle element as root
- Recursively build left and right subtrees

Time Complexity: O(n)
Space Complexity: O(log n)

Key Insight:
Choosing the middle element ensures the tree remains height-balanced.
"""

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)
