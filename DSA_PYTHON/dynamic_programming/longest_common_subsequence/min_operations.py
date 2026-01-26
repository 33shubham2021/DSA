"""
you can solve the Edit Distance problem using Longest Common Subsequence (LCS), 
but only if the allowed operations are restricted to Insertion and Deletion

Only allowed operations are insert and delete, to convert string 1 into string 2
"""
def min_operations_using_lcs(s1, s2):
    m, n = len(s1), len(s2)
    
    # --- Standard LCS DP Implementation ---
    # dp[i][j] stores length of LCS of s1[0...i-1] and s2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    lcs_len = dp[m][n]
    
    # --- Apply Formula ---
    # Deletions needed (delete non-LCS chars from s1) + Insertions needed(insert non-LCS chars of s2)
    return (m - lcs_len) + (n - lcs_len)

if __name__ == '__main__':
    s1 = "heap"
    s2 = "pea"
    print(f"Minimum operations (Insert/Delete only): {min_operations_using_lcs(s1, s2)}")
