"""
Actually, coin change 2 is easier than coin change 1
Problem - https://leetcode.com/problems/coin-change-ii/description/

"""
# This solution is accepted
def coin_change(coins, amount):
    rows = len(coins) + 1
    cols = amount + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(0, rows):
        dp[i][0] = 1
    
    for i in range(1, rows):
        for j in range(1, cols):
            if coins[i-1] <= j:
                pick = dp[i][j - coins[i-1]]
                not_pick = dp[i-1][j]
                dp[i][j] = pick + not_pick
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(coins)][amount]