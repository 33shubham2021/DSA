"""
Docstring for dynamic_programming.0_1_knapsack.0_1_knapsack
Link - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

Given W = 4, val = [1,2,3]
             wt = [4,5,1]..... 
Solve in brute force way, then optimise it using DP
Show that it has overlapping subproblem

test cases 
1. W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1] ...Ans = 3
2. W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6] ...Ans = 0
3. W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3].... Ans = 80
        

"""

# This gets accepted in GFG (link is above)
def knapsack_top_down_dp(w , val , wt):
    rows = w+1
    cols = len(val) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for index in range(cols-2,-1,-1):
        for currWeight in range(1,rows):
            if (wt[index] <= currWeight):
                dp[currWeight][index] = max(
                    val[index] + dp[currWeight-wt[index]][index+1],
                    dp[currWeight][index+1]
                )
            else:
                dp[currWeight][index] = dp[currWeight][index+1]
    return dp[w][0]





def knapsack_memoised(w , val , wt):
    rows = w+1
    cols = len(val) + 1
    dp = [[None for _ in range(cols)] for _ in range(rows)]
    return knapsack_memoised_helper(w , val , wt , 0 , dp)

def knapsack_memoised_helper(w , val , wt , currIndex , dp):
    #Base Case
    if (currIndex >= len(val)):
        return 0
    #dp check
    if (dp[w][currIndex] is not None):
        return dp[w][currIndex]
    #Choice 
    maxValue = None
    if (wt[currIndex] <= w):            # current item can be taken
        currVal = val[currIndex]
        maxValue =  max(
            currVal + knapsack_memoised_helper(w-wt[currIndex], val, wt, currIndex+1,dp),
            knapsack_memoised_helper(w, val, wt, currIndex+1,dp)
        )
    else:                               # current item cannot be taken
        maxValue =  knapsack_memoised_helper(w, val, wt, currIndex+1,dp)
    dp[w][currIndex] = maxValue
    return maxValue

def knapsack_brute_force(w , val , wt, currIndex):
    # Base case -> smallest input 
    if (currIndex >= len(val)):
        return 0
    #Choice 
    if (wt[currIndex] <= w):            # current item can be taken
        currVal = val[currIndex] 
        return max(
            currVal + knapsack_brute_force(w-wt[currIndex], val, wt, currIndex+1),
            knapsack_brute_force(w, val, wt, currIndex+1)
        )
    else:                               # current item cannot be taken
        return knapsack_brute_force(w, val, wt, currIndex+1)



def main():
    W = 5
    val = [10, 40, 30, 50]
    wt = [5, 4, 2, 3]
    print("Brute force : ",knapsack_brute_force(W,val,wt,0))
    print("Memoised : " , knapsack_memoised(W,val,wt))
    print("Iterative DP : " , knapsack_top_down_dp(W,val,wt))
    

if __name__ == "__main__":
    main()


""" SIMILAR PROBLEMS -> like 0-1 knapsack problem
Core Pattern - Take/Not take (pick/not pick)

Great question 👍
This is **exactly the right way** to master DP: *identify problem families*.

Below is a **curated list of problems that are structurally identical to 0-1 Knapsack**, i.e. **same DP state + same take / not-take choice**. I’ve grouped them so patterns are crystal clear.

---

# 🔁 0-1 Knapsack **Problem Family**

## 🔹 Core Pattern (Take / Not Take)

**State:** `dp[i][w]`
**Choice:** include item `i` or exclude it
**Constraint:** each item can be used **at most once**

---

## 1️⃣ Subset-Based Knapsack Problems (MOST IMPORTANT)

### 🔸 Subset Sum

> Can we form sum = `S` using given numbers?

* GFG: [https://www.geeksforgeeks.org/subset-sum-problem-dp-25/](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
* LeetCode 416: [https://leetcode.com/problems/partition-equal-subset-sum/](https://leetcode.com/problems/partition-equal-subset-sum/)

🧠 Transition:

```
dp[i][s] = dp[i-1][s] OR dp[i-1][s-arr[i]]
```

---

### 🔸 Partition Equal Subset Sum

> Can array be partitioned into 2 subsets of equal sum?

* GFG: [https://www.geeksforgeeks.org/partition-problem-dp-18/](https://www.geeksforgeeks.org/partition-problem-dp-18/)
* LeetCode 416: [https://leetcode.com/problems/partition-equal-subset-sum/](https://leetcode.com/problems/partition-equal-subset-sum/)

👉 Direct application of subset sum

---

### 🔸 Count of Subsets with Given Sum

> Number of subsets whose sum = S

* GFG: [https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/](https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/)
* LeetCode 494 (variation): [https://leetcode.com/problems/target-sum/](https://leetcode.com/problems/target-sum/)

🧠 Replace `max` with **count**

---

## 2️⃣ Variants Where “Value” Changes

### 🔸 Target Sum

> Assign + or − signs to reach target

* LeetCode 494: [https://leetcode.com/problems/target-sum/](https://leetcode.com/problems/target-sum/)

🧠 Transforms into **subset sum count**

---

### 🔸 Minimum Subset Sum Difference

> Partition array to minimize |S1 − S2|

* GFG: [https://www.geeksforgeeks.org/minimum-sum-partition-problem/](https://www.geeksforgeeks.org/minimum-sum-partition-problem/)
* LeetCode 2035: [https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/)

---

## 3️⃣ Coin / Count Variants (Still 0-1 style)

### 🔸 Coin Change – Limited Coins (0-1)

> Each coin can be used **once**

* GFG: [https://www.geeksforgeeks.org/coin-change-dp-7/](https://www.geeksforgeeks.org/coin-change-dp-7/)
* (Use reverse index DP → same as knapsack)

⚠️ Do **not** confuse with unbounded coin change

---

## 4️⃣ Binary String Knapsack (VERY POPULAR)

### 🔸 Ones and Zeroes

> Max number of strings using limited 0s and 1s

* LeetCode 474: [https://leetcode.com/problems/ones-and-zeroes/](https://leetcode.com/problems/ones-and-zeroes/)

🧠 This is **2D knapsack**

```
dp[i][zeros][ones]
```

---

## 5️⃣ Array DP with Capacity Constraint

### 🔸 Last Stone Weight II

> Smash stones → minimize final weight

* LeetCode 1049:
  [https://leetcode.com/problems/last-stone-weight-ii/](https://leetcode.com/problems/last-stone-weight-ii/)

🧠 Classic subset sum disguise

---

### 🔸 Rod Cutting (0-1 version)

> Each cut length usable once

* GFG: [https://www.geeksforgeeks.org/cutting-a-rod-dp-13/](https://www.geeksforgeeks.org/cutting-a-rod-dp-13/)

⚠️ Standard rod cutting is **unbounded** — specify 0-1

---

## 6️⃣ Interview Favorites (Disguised Knapsack)

### 🔸 Tallest Billboard

* LeetCode 956
  [https://leetcode.com/problems/tallest-billboard/](https://leetcode.com/problems/tallest-billboard/)

🧠 Partition + knapsack hybrid

---

### 🔸 Shopping Offers

* LeetCode 638
  [https://leetcode.com/problems/shopping-offers/](https://leetcode.com/problems/shopping-offers/)

🧠 Multi-dimensional knapsack

---

## 🧠 One-Line Rule to Identify 0-1 Knapsack

If a problem says:

✅ *choose / select / include / exclude*
✅ *each item used at most once*
✅ *maximize / minimize under a constraint*

👉 **It is 0-1 knapsack or a direct variant**

---

## 🔥 MUST-DO ORDER (Exam + Interview)

1. 0-1 Knapsack
2. Subset Sum
3. Partition Equal Subset
4. Count Subsets with Sum
5. Target Sum
6. Last Stone Weight II
7. Ones and Zeroes

Mastering these = **90% DP confidence**

---

If you want, next I can:

* Give a **single DP template** that solves all of these
* Show **how GATE/SEBI twist knapsack in MCQs**
* Provide **dry-run table comparison** across problems

Just say 👍

"""