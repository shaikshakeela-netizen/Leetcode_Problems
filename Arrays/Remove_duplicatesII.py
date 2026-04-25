'''
# Remove Duplicates from Sorted Array II

## 🧩 Problem
Given a sorted array `nums`, remove duplicates in-place such that each element appears at most twice. Return the new length `k`.

## 🚀 Approach
- Use **two pointers**
- Allow at most 2 duplicates
- Compare current element with `nums[k-2]`

## 💡 Algorithm
1. Initialize pointer `k = 2`
2. Traverse from index `2`
3. If `nums[i] != nums[k-2]`, keep the element
4. Place it at `nums[k]` and increment `k`

## ⏱ Complexity
- Time: O(n)
- Space: O(1)
'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates in-place such that each element appears at most twice.
        
        Args:
            nums (List[int]): Sorted list of integers
        
        Returns:
            int: Length of array after removing extra duplicates
        """
        if len(nums) <= 2:
            return len(nums)
        k = 2  # Pointer for position of next valid element

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k

'''
Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''
