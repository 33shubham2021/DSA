"""
Docstring for dynamic_programming.0_1_knapsack.subset_sum
Problem Link - https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
"""
# Fix this code, as per local, and add iterative DP code

def isSubsetSum (self, arr, sum):
    # code here
    rows = sum+1
    cols = len(arr) + 1
    dp = [[None for _ in range(cols)] for _ in range(rows)]
    return self.fun(arr , sum , 0, dp)
        
def fun(self, arr, sum, index, dp):
    if (index >= len(arr)):
        return False

    if (dp[sum][index] is not None):
        return dp[sum][index]
            
    ans = None
    if (arr[index] == sum):
        ans = True
    elif (arr[index] < sum):
        ans = self.fun(arr, sum-arr[index] , index+1, dp) or self.fun(arr,sum,index+1,dp)
    else :
        ans = self.fun(arr,sum,index+1,dp)
    dp[sum][index] = ans
    return ans