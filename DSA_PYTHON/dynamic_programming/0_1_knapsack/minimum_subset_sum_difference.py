"""


Subset Sum Family = Reachability problems
Here we do not need to return a value to optimise (like 0-1 knapsack), 
rather we are exploring reachability
So, DP is :
dp[i][s] = True if (pick OR not_pick is possible)

In this question, I will have to consider entire sequence to form the sums.
Therefore the base condition is when the entire array is traversed, picking/not picking elements

not pick in S1 = automatically puts the element in S2 
the choices
pick-1                                              not-1
pick-6          not-6
pick-11 not-11  pick-11 not-11                      pick-6 not-6..like this these grow

time complexity of brute force = O(2^n) (n=size of array) keeps growing by 2 in every level

Brute force works correctly for all, but time is exceeded
https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?leftPanelTabValue=SUBMISSION
"""



# this brute force is forward-recursive solution
# we go from 0 to n in index
def min_subset_sum_diff(arr , i , currSum, totalSum):
    #Base
    if i == len(arr):
        return abs((totalSum - currSum) - currSum)
    
    # choice = pick
    pick = min_subset_sum_diff(arr , i+1, currSum+arr[i],totalSum)
    not_pick = min_subset_sum_diff(arr, i+1, currSum, totalSum)
    return min(pick , not_pick) 


def min_subset_sum_diff_iterative(arr):
    n = len(arr)
    totalSum = sum(arr)

    dp = [[False] * (totalSum + 1) for _ in range(n + 1)]

    # Base case: sum 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for s in range(1, totalSum + 1):
            if arr[i-1] <= s:
                dp[i][s] = dp[i-1][s] or dp[i-1][s - arr[i-1]]
            else:
                dp[i][s] = dp[i-1][s]

    minDiff = float('inf')

    for s in range(totalSum // 2 + 1):
        if dp[n][s]:
            minDiff = min(minDiff, totalSum - 2*s)

    return minDiff


if __name__ == '__main__':
    arr = [1, 6, 11, 5]
    totalSum = sum(arr)
    print(min_subset_sum_diff(arr, 0, 0, totalSum))