"""
Problem - https://www.geeksforgeeks.org/dsa/count-of-subsets-with-sum-equal-to-x/
In the above problem, 0s are also considered, special case, otherwise memoised version works fine
https://www.naukri.com/code360/problems/number-of-subsets_3952532?leftPanelTabValue=PROBLEM
Above problem submission will work
"""


def count_subset_sum_memoised(arr , target , index , dp):
    if (target == 0):
        return 1
    #Base case
    if (index >= len(arr) or target < 0):
        return 0
    
    if (dp[index][target] is not None):
        return dp[index][target]

    ans = None
    if (arr[index] > target):
        ans = count_subset_sum_memoised(arr , target , index+1, dp)
    
    ans = (
        count_subset_sum_memoised(arr , target-arr[index] , index+1, dp) +
        count_subset_sum_memoised(arr , target , index+1 , dp)
    )
    dp[index][target] = ans
    return ans

def count_subset_sum_recursive(arr, target, index):
    if (target == 0):
        return 1
    #Base case
    if (index >= len(arr)):
        return 0
    
    if (arr[index] > target):
        return count_subset_sum_recursive(arr , target , index+1)
    
    return (
        count_subset_sum_recursive(arr , target-arr[index] , index+1) +
        count_subset_sum_recursive(arr , target , index+1)
    )
    
if __name__ == '__main__':
    # arr1 = [5, 2, 3, 10, 6, 8]
    # t1 = 10
    # e1 = 3
    # print(e1 == count_subset_sum_recursive(arr1 , t1 , 0))

    # arr2 = [2, 5, 1, 4, 3],
    # t2 = 10
    # e2 = 3
    # print(e2 == count_subset_sum_recursive(arr2 , t2 , 0))

    # arr3 = [5, 7, 8],
    # t3 = 3
    # e3 = 0
    # print(e3 == count_subset_sum_recursive(arr3 , t3 , 0))

    # # arr4 = [35, 2, 8, 22]
    # # t4 = 0
    # # e4 = 1
    # # print(e4 == count_subset_sum_recursive(arr4 , t4 , 0))

    arr = [12, 14, 3, 18, 2]
    target = 13
    rows = len(arr) + 1
    cols = target + 1
    dp = [[None for _ in range(cols)] for _ in range(rows)]
    print(count_subset_sum_memoised(arr , target , 0 , dp))
    