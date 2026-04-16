'''
Leetcode Problem : 
" Given an array of integers nums and a target value, return the sum of three integers in nums such that the sum is closest to the target. "
Leetcode number: 16

💡 Approach (Two Pointer Technique)
# Sort the array
# Fix one number
# Use two pointers (left, right) to find the best pair
# Keep updating the closest sum

🧠 Time Complexity
O(n²) → Efficient for this problem
'''

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        # Step 2: Initialize closest sum
        closest = nums[0] + nums[1] + nums[2]
        # Step 3: Iterate through array
        for i in range(len(nums) - 2):
            # Skip duplicate values (optimization)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            # Step 4: Two-pointer approach
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # Update closest sum
                if abs(total - target) < abs(closest - target):
                    closest = total
                # Move pointers based on comparison
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # Perfect match
        return closest


'''
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
