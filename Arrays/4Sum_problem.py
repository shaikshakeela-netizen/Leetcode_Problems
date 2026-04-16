'''
4Sum Problem
 Leetcode number: 18

**Problem: 
Given an array nums and a target value, return all unique quadruplets [a, b, c, d] such that:
a + b + c + d = target

** Approach (Sorting + Two Pointers)
# Sort the array
# Fix two numbers (i, j)
# Use two pointers (left, right) for the remaining two
# Skip duplicates to avoid repeated results

**Time Complexity
# O(n³)
# (Three nested loops + two-pointer scan)
'''

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        # Fix first element
        for i in range(n - 3):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Fix second element
            for j in range(i + 1, n - 2):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                # Two-pointer approach
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for right
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result

  '''
  Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''
