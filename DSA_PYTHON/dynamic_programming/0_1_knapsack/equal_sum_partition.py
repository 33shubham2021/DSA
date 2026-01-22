"""
Problem - https://leetcode.com/problems/partition-equal-subset-sum/description/
Application of subset sum problem 
"""

def solve(arr):
    
    totalSum = sum(arr)
    if (totalSum % 2 is not 0):
        return False
    
    target = totalSum // 2
    return isSubsetSum(arr , target)


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