"""
Problem - https://leetcode.com/problems/longest-common-subsequence/description/

Print LCS - https://www.naukri.com/code360/problems/print-longest-common-subsequence_8416383?leftPanelTabValue=SUBMISSION


if s1[i1] == s2[i2] // there is a match
    
    in the the smaller subsequences (be it max or anything), 
    definitly current char can be appended to smaller answer

    LCS of length 1 is found. If some LCS of length 2 exists, then it must include the 
    current common character, as wee have to deal with LCS
else 
    we will have to consider both

TODO - https://www.geeksforgeeks.org/problems/print-all-lcs-sequences3413/1
TODO - print LCS, using LCS -> this will be space efficient 

"""

def get_LCS(s1, s2):
    rows = len(s1) + 1
    cols = len(s2) + 1
    dp = [["" for _ in range(cols)] for _ in range(rows)]
    for i1 in range(rows-2, -1, -1):
        for i2 in range(cols-2, -1, -1):
            if (s1[i1] == s2[i2]):
                dp[i1][i2] = s1[i1] + dp[i1 + 1][i2 + 1]
            else:
                r1 = dp[i1 + 1][i2] 
                r2 = dp[i1][i2 + 1]
                if len(r1) >= len(r2):
                    dp[i1][i2] = r1
                else:
                    dp[i1][i2] = r2
    return dp[0][0]
    

def LCS(s1, s2):
    rows = len(s1) + 1
    cols = len(s2) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    # Base case if already satisfied while initialising dp array (=0)

    for i1 in range(rows-2, -1, -1):
        for i2 in range(cols-2, -1, -1):
            if (s1[i1] == s2[i2]):
                dp[i1][i2] = 1 + dp[i1 + 1][i2 + 1]
            else:
                dp[i1][i2] = max(
                    dp[i1 + 1][i2] , dp[i1][i2 + 1]
                )
    return dp[0][0]


def LCS_memoised(s1, s2, i1, i2, dp):
    #Base 
    if (i1 == len(s1) or i2 == len(s2)):
        return 0

    if (dp[i1][i2] is not None):
        return dp[i1][i2]
    
    if (s1[i1] == s2[i2]): # match
        dp[i1][i2] =  1 + LCS_memoised(s1, s2, i1+1, i2+1, dp)
    else:
        dp[i1][i2] = max(
            LCS_memoised(s1, s2, i1+1, i2, dp),
            LCS_memoised(s1, s2, i1, i2+1, dp)
        )
    return dp[i1][i2]


def LCS_recursive(s1, s2):
    #Base 
    if (len(s1) == 0 or len(s2) == 0):
        return 0

    if (s1[0] == s2[0]): # match
        return 1 + LCS_recursive(s1[1:] , s2[1:])
    else:
        return max(
            LCS_recursive(s1[1:] , s2),
            LCS_recursive(s1, s2[1:])
        )

if __name__ == "__main__":
    print("####  LCS  ####")
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print(LCS_recursive(s1 , s2))
    
    rows = len(s1)
    cols = len(s2)
    dp = [[None for _ in range(cols)] for _ in range(rows)]
    print(LCS_memoised(s1, s2, 0, 0, dp))

    print("Length of LCS is ",LCS(s1, s2))
    print("The value of LCS is ",get_LCS(s1, s2))