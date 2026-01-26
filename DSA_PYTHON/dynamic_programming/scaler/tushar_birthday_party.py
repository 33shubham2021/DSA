"""
Problem - https://www.scaler.com/academy/mentee-dashboard/class/75278/homework/problems/385/submissions
"""

def solve(A, B, C):
    W = max(A)
    rows = len(B) + 1
    cols = W + 1
    dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    for i in range(len(B) + 1):
        dp[i][0] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            exclude_cost = float('inf')
            if (dp[i-1][j] != float('inf')):
                exclude_cost = dp[i-1][j]
            if (B[i-1] <= j):
                include_cost = float('inf')
                if (dp[i][j - B[i-1]] != float('inf')):
                    include_cost = C[i-1] + dp[i][j - B[i-1]]
                dp[i][j] = min(include_cost, exclude_cost)
            else:
                dp[i][j] = exclude_cost
    
    total_cost = 0
    for friend_cap in A:
        total_cost += dp[len(B)][friend_cap]
    return total_cost

if __name__ == "__main__":
    pass