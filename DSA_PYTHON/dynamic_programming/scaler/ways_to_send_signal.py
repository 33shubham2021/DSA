"""
Problem - https://www.scaler.com/academy/mentee-dashboard/class/75278/homework/problems/4806/submissions
"""
def solution(A):
    rows = A + 2
    dp = [0 for _ in range(rows)]
        
    mod = 1000000000 + 7
    dp[0] = 1
    dp[1] = 2
    for i in range(2, rows):
        dp[i] = (dp[i-1] + dp[i-2]) % mod
    return dp[A]    