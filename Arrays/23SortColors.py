'''
leetcode number:75
Given an array nums containing 0, 1, and 2:

0 → Red
1 → White
2 → Blue

Sort the array in-place without using built-in sort.

💡 Approach: Three Pointers

We use:

low → position for next 0
mid → current element
high → position for next 2
🧠 Algorithm
If nums[mid] == 0 → swap with low, move both
If nums[mid] == 1 → move mid
If nums[mid] == 2 → swap with high, move high

'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the array in-place using Dutch National Flag algorithm.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Place 0 at correct position
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # 1 is already in correct region
                mid += 1

            else:
                # Place 2 at correct position
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1



'''
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 '''
