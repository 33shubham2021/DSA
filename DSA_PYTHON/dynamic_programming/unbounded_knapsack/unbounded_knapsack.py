"""
Docstring for dynamic_programming.unbounded_knapsack.unbounded_knapsack
Problem - https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1

"""
# Iterative DP, this is accepted on GFG
def unbounded_knapsack(w, val, wt, n):
    rows = n+1
    cols = w+1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # i == n, j == w
    for i in range(rows):
        for j in range(cols):
            if (wt[i-1] <= j):
                dp[i][j] = max(
                    val[i-1] + dp[i][j-wt[i-1]], dp[i-1][j]
                )
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]



def unbounded_knapsack_recursive(w, val, wt, n):
    # if empty array, then nothing to pick
    if (n == 0 or w == 0):
        return 0
    if (wt[n-1] <= w):
        return max(
            val[n-1] + unbounded_knapsack_recursive(w-wt[n-1] , val, wt, n),
            unbounded_knapsack_recursive(w, val, wt, n-1)
        )
    else:
        return unbounded_knapsack_recursive(w, val, wt, n-1)


if __name__ == "__main__":
    val = [10, 40, 50, 70]
    wt = [1, 3, 4, 5]
    w = 8
    out = 110
    print(out == unbounded_knapsack_recursive(w, val, wt, len(val)))

    val1 = [1, 1]
    wt1 = [2, 1]
    w1 = 3
    out1 = 3
    print(out1 == unbounded_knapsack_recursive(w1, val1, wt1, len(val1)))

    val2 = [6, 8, 7, 100]
    wt2 = [2, 13, 4, 5]
    w2 = 1
    out2 = 0
    print(out2 == unbounded_knapsack_recursive(w2, val2, wt2, len(val2)))

    print("Iterative is : ",out == unbounded_knapsack(w, val, wt, len(val)))
    print("Iterative is : ",out1 == unbounded_knapsack(w1, val1, wt1, len(val1)))
    print("Iterative is : ",out2 == unbounded_knapsack(w2, val2, wt2, len(val2)))

    