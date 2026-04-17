
'''
** Problem Title
Next Permutation

🔢 Problem Number
LeetCode 31

🧩 Problem Statement

"" Given an integer array nums, find the next lexicographically greater permutation of numbers.

If such an arrangement is not possible, rearrange it as the lowest possible order (ascending).

The replacement must be in-place and use only constant extra memory.""

🧠 Approach (Step-by-Step)

We follow 3 key steps:

🔹 Step 1: Find Breakpoint
Traverse from right
Find first index i such that:
nums[i] < nums[i + 1]

This is where the next permutation change begins
🔹 Step 2: Find Next Greater Element
From right side, find element just greater than nums[i]
Swap them

🔹 Step 3: Reverse the Suffix
Reverse elements from i+1 to end
This ensures the smallest possible next permutation'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        #find the break point
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        
        #if Break point exists
        if i >=0:
            j=n-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i], nums[j]= nums[j], nums[i]
        
        left, right= i+1, n-1
        while left < right :
            nums[left], nums[right]= nums[right], nums[left]
            left+=1
            right-=1

'''
Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 '''
        

