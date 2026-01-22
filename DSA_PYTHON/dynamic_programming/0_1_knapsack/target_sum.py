"""
Problem - https://leetcode.com/problems/target-sum/
arr = [1,1,2,3]
sum = 1
we have to assign + or - to each element in the array and return 
the count of such sequences which result to sum=1
Ans of above = 3 
                1+1+2-3 , 1-1-2+3, -1+1-2+3
1st observation - we need the entire array for obtaining one value to check
Basically, we want to check "reachability" here
so, backtracking will be a better way than DP
iterative dp will require some modifications, so memoised version is the best -> initially

TODO - solve this in memoised version and submit
"""

def target_sum_memoised(arr , n , target, dp):
    if (n == 0):
        if target == 0:
            return 1
        else:
            return 0
    
    if (dp[n][target] is not None):
        return dp[n][target]

    dp[n][target] =  (
        target_sum_memoised(arr,n-1,target + arr[n-1], dp) + 
        target_sum_memoised(arr , n-1, target - arr[n-1], dp)
    )
    return dp[n][target]



def target_sum(arr, n, target):
    if (n == 0):
        if target == 0:
            return 1
        else:
            return 0
    
    return (
        target_sum(arr,n-1,target + arr[n-1]) + 
        target_sum(arr , n-1, target - arr[n-1])
    )