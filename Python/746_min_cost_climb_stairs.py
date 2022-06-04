'''
This file implements the solution to the min cost climbing stairs problem. The idea is to identify that the cost to climb to the top from ith step
is dependent on the cost to climb to top from i+1 step to the top or i+2 step to the top. (this is top down, but bottom up is very similar. For bottom
up you think of the cost to climb to the ith step (including using that step))

dp[i] = cost[i] + min(dp[i-1], dp[i-2])

Time Complexity: O(n)
Space Complexity: O(n)

Problem Link: https://leetcode.com/problems/min-cost-climbing-stairs/
'''


from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[-1], dp[-2] = cost[-1], cost[-2]
        
        for i in range(3, len(cost)+1):
            dp[-i] = cost[-i] + min(dp[-i+1], dp[-i+2])
        
        return min(dp[0], dp[1])