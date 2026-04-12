""" 
Problem : Two Sum
Leetcode_Number : 1
Steps: 
1. First fix element using index i
2. Loop through remaining elements using j
3. check if sums are equals to target
4. If yes -> retrun indices
"""  
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Function to find indices of two numbers that sum to target

        Parameters:
        nums (List[int]): List of integers
        target (int): Target sum

        Returns:
        List[int]: Indices of the two numbers
        """

        # Step 1: Iterate through each element
        for i in range(len(nums)):

            # Step 2: Check with remaining elements
            for j in range(i + 1, len(nums)):

                # Step 3: Check if current pair sums to target
                if nums[i] + nums[j] == target:

                    # Step 4: Return indices immediately when found
                    return [i, j]


# -------------------------
# 🔍 Example Test Case
# -------------------------
if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    result = solution.twoSum(nums, target)

    print("Input:", nums)
    print("Target:", target)
    print("Output (Indices):", result)

"""
Expected Output:
Input: [2, 7, 11, 15]
Target: 9
Output (Indices): [0, 1]
"""

