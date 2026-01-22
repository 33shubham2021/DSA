"""
Docstring for dynamic_programming.0_1_knapsack.subset_sum_v2
Below code works fine, and is easier to code as well  (filling up the dp array)
"""
def isSubsetSum(arr , target):
    n = len(arr)
    rows = n + 1
    cols = target+1
    dp = [[False for _ in range(cols)] for _ in range(rows)]
    for i in range(0,rows):
        dp[i][0] = True

    # i == n, j == target/sum
    for i in range(1 , rows):
        for j in range(1 , cols):
            if (arr[i-1] <= j):
                dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]


def main():
    arr1 = [3, 34, 4, 12, 5, 2]
    sum1 = 9
    print(isSubsetSum(arr1 , sum1))
    arr2 = [11, 48, 24]
    sum2 = 83
    print(isSubsetSum(arr2 , sum2))

if __name__ == "__main__":
    main()