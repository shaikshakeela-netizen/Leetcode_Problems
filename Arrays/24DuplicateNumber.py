'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number, return this repeated number.

⚠️ Constraints:
Do not modify the array
Use only constant extra space
🔢 Problem Number

LeetCode 287 – Find the Duplicate Number

🚀 Approach (Floyd’s Cycle Detection – Tortoise & Hare)
💡 Intuition:
Treat the array like a linked list
Index → Node
Value → Next pointer
Since one number is duplicated → it creates a cycle
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
     
        slow = nums[0]
        fast = nums[0]

        # Step 1: Detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]   #  move 2 steps
            if slow == fast:
                break

        # Step 2: Find duplicate (cycle start)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


'''
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 '''
