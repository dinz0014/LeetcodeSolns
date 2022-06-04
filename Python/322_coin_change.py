'''
This file implements the solution to the coin change problem. The optimal subproblems are
dp[i] = minimum number of coins required to make amount i

dp[i] = min{ dp[i-c] for c in coins} + 1. To make up amount i with a coins list, we check how many coins were required to make up i-coins[j] for all j.
Take the minimum of that value and add 1 to make up i.

Time Complexity: O(NC) where C is size of coins and N is amount
Space Complexity: O(N)

Problem Link: https://leetcode.com/problems/coin-change/
'''

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if not coins:
            return -1
        
        # Maximum coins we need to make amount is obviously amount. So, for comparison we initialise DP with amount+1 everywhere
        MAX = amount + 1
        dp = [MAX]*MAX
        # Base Case
        dp[0] = 0
        
        # Iterate over all amounts and coins and update DP
        for i in range(amount+1):                           
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        return dp[-1] if dp[-1] != MAX else -1