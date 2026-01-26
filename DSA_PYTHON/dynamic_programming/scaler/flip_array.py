"""
Docstring for dynamic_programming.scaler.flip_array
"""

def min_flips(arr):
    total_sum = sum(arr)
    target = total_sum // 2
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for num in arr:
       for j in range(target, num - 1, -1):
           if dp[j - num] != float('inf'):
               dp[j] = min(dp[j], dp[j - num] + 1)
    
    for i in range(target, -1, -1):
        if dp[i] != float('inf'):
            return dp[i]
            
    return 0

def fun(arr, curSum, flips, n):
        if n == 0:
            if curSum <= 0:
                return (float('inf'), float('inf'))
            else:
                return (curSum, flips)
        
        flip = fun(arr, curSum-arr[n-1], flips+1, n-1)
        not_flip = fun(arr, curSum+arr[n-1], flips, n-1)
        return min(flip, not_flip)

