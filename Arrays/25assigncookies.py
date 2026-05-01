'''
Assign Cookies
📌 Problem Statement

You are given two integer arrays:

g[i] → greed factor of each child
s[j] → size of each cookie

Each child can get at most one cookie. A child is satisfied if:

s[j] >= g[i]

👉 Return the maximum number of satisfied children.

💡 Approach (Greedy + Two Pointers)
Sort both arrays:
Assign smallest cookie to least greedy child
Use two pointers:
i → tracks children
j → tracks cookies
If current cookie satisfies child:
Move to next child (i += 1)
Always move cookie pointer (j += 1)

👉 This ensures optimal matching with minimum waste.

🧠 Key Insight

Give the smallest possible cookie that satisfies a child →
this leaves bigger cookies for greedier children.
'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0  # child pointer
        j = 0  # cookie pointer
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        
        return i


'''
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
'''
