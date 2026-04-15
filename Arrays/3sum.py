'''
leetcode problem : 3sum
leetcode number; 15
Approach: Sorting + Two Pointers
Steps:
Sort the array
Fix one element (i)
Use two pointers (left, right) to find pairs
Skip duplicates to ensure unique triplets
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result



'''
Input:

nums = [-1, 0, 1, 2, -1, -4]

After sorting:

[-4, -1, -1, 0, 1, 2]

Valid Triplets:
[-1, -1, 2]
[-1, 0, 1]
'''
