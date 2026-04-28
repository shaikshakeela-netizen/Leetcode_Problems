'''📌 Problem: Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result must be unique, and you may return the result in any order.


🚀 Approach

To efficiently solve this problem, we use the concept of hashing with sets:

Convert nums1 into a set → this removes duplicates and allows O(1) lookup.
Traverse through nums2.
For each element:
Check if it exists in the set created from nums1.
If yes, add it to a result set (ensures uniqueness).
Convert the result set back to a list and return.
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = set()

        for num in nums2:
            if num in set1:
                result.add(num)

        return list(result)

  '''
  Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 
'''
