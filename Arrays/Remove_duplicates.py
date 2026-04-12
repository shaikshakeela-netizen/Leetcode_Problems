"""
Problem: Remove Duplicates from Sorted Array
LeetCode_Number: 26
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates in-place and returns count of unique elements

        Parameters:
        nums (List[int]): Sorted list of integers

        Returns:
        int: Number of unique elements (k)
        """
        # Edge case: empty array
        if not nums:
            return 0
        # Pointer i tracks last unique element
        i = 0
        # Pointer j scans the array
        for j in range(1, len(nums)):
            # If new unique element is found
            if nums[j] != nums[i]:
                i += 1              # move i forward
                nums[i] = nums[j]   # place new unique element

        # Length of unique elements = i + 1
        return i + 1


# -------------------------
# 🔍 Example Test Case
# -------------------------
if __name__ == "__main__":
    solution = Solution()

    nums = [0,0,1,1,1,2,2,3,3,4]

    k = solution.removeDuplicates(nums)

    print("Unique Count:", k)
    print("Modified Array:", nums[:k])  # only first k elements are valid


"""
Expected Output:
Unique Count: 5
Modified Array: [0, 1, 2, 3, 4]
"""
