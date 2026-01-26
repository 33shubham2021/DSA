"""
Docstring for dynamic_programming.edit_distance
Problem - https://leetcode.com/problems/edit-distance/description/
Explanation - https://www.youtube.com/watch?v=XYi2-LPrwm4
"""

def edit_distance(s1, s2):
    rows = len(s1) + 1
    cols = len(s2) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for j in range(1,cols):
        dp[0][j] = j
    for i in range(1,rows):
        dp[i][0] = i
    
    for i in range(1,rows):
        for j in range(1,cols):
            if (s1[i-1] == s2[j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(1 + dp[i][j-1], 
                            1 + dp[i-1][j], 
                            1 + dp[i-1][j-1])
    return dp[len(s1)][len(s2)]

def edit_distance_recursive(s1, s2, i, j):
    #Base case
    if (i == len(s1) or j == len(s2)): # reached the end
        return max(len(s1)-i , len(s2)-j)
    
    if (s1[i] == s2[j]): # curr chars are equal
        return edit_distance_recursive(s1, s2, i+1, j+1)
    else:
        insert = 1 + edit_distance_recursive(s1, s2, i, j+1)
        delete = 1 + edit_distance_recursive(s1, s2, i+1, j)
        replace = 1 + edit_distance_recursive(s1, s2, i+1, j+1)
        return min(insert, delete, replace)

if __name__ == "__main__":
    s1 = "intention"
    s2 = "execution"
    o1 = 5
    print(o1 == edit_distance_recursive(s1, s2, 0, 0))

    ss1 = "abcd"
    ss2 = "bcfe"
    o2 = 3
    print(o2 == edit_distance_recursive(ss1, ss2, 0, 0))

    print(edit_distance(s1,s2) == o1)
    print(edit_distance(ss1,ss2) == o2)


    
