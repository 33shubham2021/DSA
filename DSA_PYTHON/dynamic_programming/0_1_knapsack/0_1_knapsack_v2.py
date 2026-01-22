"""
This file contains the code of 0-1 knapsack, as per aditya verma's youtube videos
Link - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
in this version, it's easier to fill the dp array, without much errors
I am trying to code every dp problem in this manner 
"""


def knapsack_iterative_dp(w, val, wt, n):
    rows = n+1
    cols = w+1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    #Base case is already handled in the above line (see below 2 lines for understanding)
    
    for i in range(1,rows):
        for j in range(1,cols):
            if (wt[i-1] <= j):
                currVal = val[i-1]
                dp[i][j] = max(dp[i-1][j] , currVal + dp[i-1][j - wt[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]




def knapsack_brute_force(w , val , wt, n):
    # Index pointing at is one less than size n
    currIndex = n-1
    # Base case -> smallest input 
    if (currIndex < 0):
        return 0
    #Choice 
    if (wt[currIndex] <= w):            # current item can be taken
        currVal = val[currIndex] 
        return max(
            currVal + knapsack_brute_force(w-wt[currIndex], val, wt, n-1),
            knapsack_brute_force(w, val, wt, n-1)
        )
    else:                               # current item cannot be taken
        return knapsack_brute_force(w, val, wt, n-1)



def main():
    W = 5
    val = [10, 40, 30, 50]
    wt = [5, 4, 2, 3]
    print("Brute force : ",knapsack_brute_force(W,val,wt,len(val)))
    print("Iterative DP : ",knapsack_iterative_dp(W,val,wt,len(val)))

if __name__ == "__main__":
    main()