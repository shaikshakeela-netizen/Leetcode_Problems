'''
👇

📌 Problem: Move Zeroes

Given an integer array nums, move all 0s to the end of the array while maintaining the relative order of the non-zero elements.
🚀 Approach (Two-Pointer Technique)

We use a two-pointer approach to efficiently rearrange the array:

Initialize a pointer j = 0 → this tracks the position to place the next non-zero element.
Traverse the array using pointer i.
If nums[i] != 0:
Swap nums[i] with nums[j]
Increment j
This ensures:
All non-zero elements move to the front
Zeroes automatically shift to the end
'''
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    j = 0

    for i in range(n):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1




'''
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 '''
