'''
🔢 Problem Number

LeetCode 33

🧩 Problem Statement

Given a rotated sorted array nums (with distinct integers) and a target value, return the index of the target if it exists. Otherwise, return -1.

👉 The algorithm must run in O(log n) time.

**Approach (Binary Search Logic):
Even though the array is rotated, one half is always sorted.
🔍 Key Idea:
At every step:
Check which half is sorted
Decide whether target lies in that half
Move accordingly

'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # Found target
            if nums[mid] == target:
                return mid
            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


'''
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''
