"""
Problem: Search Insert Position
Leetcode_Number :035

Problem Understanding:
Given a sorted array of distinct integers and a target value,
return the index if the target is found.

If not, return the index where it would be inserted 
to maintain sorted order.

Example:
Input: nums = [1,3,5,6], target = 5  → Output: 2
Input: nums = [1,3,5,6], target = 2  → Output: 1
Input: nums = [1,3,5,6], target = 7  → Output: 4

-----------------------------------------------------
 Approach: Binary Search

Idea:
Since the array is sorted, we use binary search:
1. Find middle element
2. Compare with target
3. Narrow search space:
   - If target is larger → move right
   - If smaller → move left
4. If not found:
   👉 `left` will be the correct insertion position

-----------------------------------------------------
⏱ Time Complexity: O(log n)
📦 Space Complexity: O(1)

-----------------------------------------------------
🚀 Key Insight:
Even if target is not found, `left` always points to the correct 
position where target should be inserted.
"""

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Finds index of target or insert position

        Parameters:
        nums (List[int]): Sorted list of integers
        target (int): Value to search

        Returns:
        int: Index of target or insertion position
        """

        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Find middle index
            mid = (left + right) // 2
            # Case 1: Target found
            if nums[mid] == target:
                return mid
            # Case 2: Target is greater → search right half
            elif nums[mid] < target:
                left = mid + 1
            # Case 3: Target is smaller → search left half
            else:
                right = mid - 1
        # If not found, left is the correct insert position
        return left


# -------------------------
# 🔍 Example Test Cases
# -------------------------
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([1, 3, 5, 6], 0)
    ]
    for nums, target in test_cases:
        result = solution.searchInsert(nums, target)
        print(f"Array: {nums}")
        print(f"Target: {target}")
        print(f"Insert Position: {result}\n")


"""
Expected Output:

Array: [1, 3, 5, 6]
Target: 5
Insert Position: 2

Array: [1, 3, 5, 6]
Target: 2
Insert Position: 1

Array: [1, 3, 5, 6]
Target: 7
Insert Position: 4

Array: [1, 3, 5, 6]
Target: 0
Insert Position: 0
"""
