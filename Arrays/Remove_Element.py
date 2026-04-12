"""
Problem: Remove Element
LeetCode_Number:027
"""
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      # Pointer k → position for next valid element
        k = 0
        # Traverse entire array
        for i in range(len(nums)):
            # If current element is NOT equal to val
            if nums[i] != val:
                # Place it at index k
                nums[k] = nums[i]
                # Move k forward
                k += 1
        # k is the count of valid elements
        return k
# -------------------------
#  Example Test Case
# -------------------------
if __name__ == "__main__":
    solution = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    print("Value to remove:", val)
    print("New Length (k):", k)
    print("Modified Array:", nums[:k])


"""
Expected Output:
Value to remove: 3
New Length (k): 2
Modified Array: [2, 2]
"""
