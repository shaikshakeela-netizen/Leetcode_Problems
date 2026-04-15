'''
leetcode_problem : 11
problem : container with the most water

Approach: Two Pointer Technique

Instead of checking all pairs (which is slow), we use two pointers:

Start from both ends of the array
Calculate area at each step
Move the pointer with the smaller height
'''

class Solution:
    def maxArea(self, height):
        # Initialize two pointers
        left, right = 0, len(height) - 1        
        # Variable to store maximum water
        max_water = 0        
        while left < right:
            # Calculate width between two lines
            width = right - left            
            # Find the minimum height
            h = min(height[left], height[right])            
            # Calculate area
            area = width * h            
            # Update maximum water
            max_water = max(max_water, area) 
          
            # Move the pointer pointing to smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1        
        return max_water
