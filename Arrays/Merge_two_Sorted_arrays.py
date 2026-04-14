'''
problem: Merge two sorted arrays
Leetcode : 88
'''

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 as one sorted array (in-place).

        Approach:
        - Use three pointers starting from the end
        - Avoid overwriting elements in nums1
        """
        # Pointer for nums1 (last valid element)
        i = m - 1        
        # Pointer for nums2
        j = n - 1        
        # Pointer for placement in nums1
        k = m + n - 1
        # Merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # Copy remaining elements of nums2 (if any)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1



'''
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
Compare 3 and 6 → place 6
Compare 3 and 5 → place 5
Compare 3 and 2 → place 3
Compare 2 and 2 → place 2
...
Final: [1,2,2,3,5,6]
'''
