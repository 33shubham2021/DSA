"""
Problem - https://leetcode.com/problems/coin-change/submissions/1892848692/
"""

def coin_change(coins, amount):
    rows = len(coins) + 1
    cols = amount + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(1, cols):
        dp[0][i] = -1
    
    for i in range(1, rows):
        for j in range(1, cols):
            if coins[i-1] <= j:
                pick = dp[i][j - coins[i-1]]
                if pick != -1:
                    pick = 1 + pick
                not_pick = dp[i-1][j]
                if pick != -1 and not_pick != -1:
                    dp[i][j] = min(pick, not_pick)
                elif pick != -1:
                    dp[i][j] = pick
                else:
                    dp[i][j] = not_pick
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(coins)][amount]


def coin_change_recursive(coins , amount, n):
    #Base case
    if (amount == 0):
        return 0
    if (n == 0):
        return -1
    

    if (coins[n-1] <= amount):
        #pick
        pick = coin_change_recursive(coins, amount - coins[n-1], n)
        if pick != -1:
            pick = 1 + pick

        # Not pick
        not_pick = coin_change_recursive(coins, amount, n-1)

        # Decide
        if pick != -1 and not_pick != -1:
            return min(pick, not_pick)
        elif pick != -1:
            return pick
        else:
            return not_pick
    else:
        return coin_change_recursive(coins , amount, n-1)
    
if __name__ == "__main__":
    c1 = [1,2,5]
    a1 = 11
    o1 = 3
    print(o1 == coin_change_recursive(c1 , a1, len(c1)))

    c2 = [2]
    a2 = 3
    o2 = -1
    print(o2 == coin_change_recursive(c2 , a2, len(c2)))

    c3 = [1]
    a3 = 0
    o3 = 0
    print(o3 == coin_change_recursive(c3 , a3, len(c3)))

    print("Iterative DP : ", o1 == coin_change(c1,a1))
    print("Iterative DP : ", o2 == coin_change(c2,a2))
    print("Iterative DP : ", o3 == coin_change(c3,a3))


