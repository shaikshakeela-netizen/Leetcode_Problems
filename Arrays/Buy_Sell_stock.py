'''
Problem Title

Best Time to Buy and Sell Stock

🔢 Problem Number

LeetCode 121

🧩 Problem Statement

You are given an array prices where prices[i] is the price of a given stock on day i.

👉 You want to maximize your profit by choosing:

One day to buy
A different day in the future to sell

👉 Return the maximum profit you can achieve.
👉 If no profit is possible, return 0.

🧠 Approach (Single Pass Optimization)
🔑 Key Idea:
Track the minimum price so far
At each step, calculate profit if sold today
Keep updating the maximum profit
'''

"""
LeetCode 121: Best Time to Buy and Sell Stock

Approach:
- Traverse the array once
- Track minimum price so far
- Calculate profit at each step

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize to infinity
        max_profit = 0

        for price in prices:
            # Update minimum price
            if price < min_price:
                min_price = price

            # Calculate profit
            profit = price - min_price
            # Update maximum profit
            if profit > max_profit:
                max_profit = profit
        return max_profit


'''
example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 '''
