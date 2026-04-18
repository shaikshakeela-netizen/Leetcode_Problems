'''
📌 Problem Title

Find First and Last Position of Element in Sorted Array

🔢 Problem Number

LeetCode 34

🧩 Problem Statement

Given a sorted array of integers nums and a target value, return the starting and ending position of the target.

👉 If the target is not found, return [-1, -1]
👉 Must run in O(log n) time

Approach (Binary Search Twice)

We perform two binary searches:

🔹 1. Find First Occurrence
When nums[mid] == target
Move left to find earlier occurrence
2. Find Last Occurrence
When nums[mid] == target
Move right to find later occurrencefrom typing import List
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1   # move left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans
        def findLast():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1   # move right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [findFirst(), findLast()]
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
