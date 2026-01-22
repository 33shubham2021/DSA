"""
Docstring for dynamic_programming.unbounded_knapsack.rod_cutting
problem - https://www.geeksforgeeks.org/problems/rod-cutting0840/1
"""
# This version (iterative DP) is accepted in GFG
def rod_cutting(price):
    l = len(price) #current length of rod
    n = len(price) #current cutting length
    rows = n+1
    cols = l+1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # i==current processing length that is to be cut, j=current length of rod
    # i==n, j==l
    for i in range(1,rows):
        for j in range(1,cols):
            if (i <= j):   
                dp[i][j] = max(
                    dp[i-1][j],                 # no cut
                    price[i-1] + dp[i][j - i]     # made the cut
                )
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][l]
    


def rod_cutting_recursive(price, l, n):
    """Given the price array, I am processing rod of length=l, and currently making a cut of size n"""    
    # Base case
    if n == 0 or l == 0:
        return 0
    if (n > l):
        return rod_cutting_recursive(price , l, n-1)
    return max(
        rod_cutting_recursive(price, l, n-1),               #not making the cut
        price[n-1] + rod_cutting_recursive(price, l-n, n)   #making the cut
    )




if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    ans = rod_cutting_recursive(price, len(price), len(price))
    out = 22
    print(ans == out)

    price1 = [3, 5, 8, 9, 10, 17, 17, 20]
    out1 = 24
    ans1 = rod_cutting_recursive(price1, len(price1), len(price1))
    print(ans1 == out1)

    price2 = [3]
    out2 = 3
    ans2 = rod_cutting_recursive(price2, len(price2), len(price2))
    print(ans2 == out2)

    print("Iterative ; ",rod_cutting(price) == out)
    print("Iterative ; ",rod_cutting(price1) == out1)
    print("Iterative ; ",rod_cutting(price2) == out2)
