"""
Problem - https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1
Memoised version also works fine, but gives time limit exceeds error
TODO - try writing and submitting iterative dp version 
       watch this - https://www.youtube.com/watch?v=odrfUCS9sQk
"""

def LIS(arr):
    n = len(arr)
    dp = [[0 for _ in range(n+1) for _ in range(n+1)]]

    for curr in range(n - 1, -1, -1):
        for prev in range(curr - 1, -2, -1): # prev goes from curr-1 down to -1
            len_exclude = dp[curr + 1][prev + 1]

            len_include = 0
            if prev == -1 or arr[curr] > arr[prev]:
                len_include = 1 + dp[curr + 1][curr + 1]
            
            dp[curr][prev + 1] = max(len_include, len_exclude)
            
    return dp[0][0]


def LIS_memoised(arr, curr_index, prev_index, dp):
    if curr_index == len(arr):
        return 0
    
    if (dp[curr_index][prev_index + 1] is not None):
        return dp[curr_index][prev_index + 1]
    
    exclude = LIS_memoised(arr, curr_index+1, prev_index, dp)
    include = 0
    if (prev_index == -1 or arr[curr_index] > arr[prev_index]):
        include = 1 + LIS_memoised(arr, curr_index+1, curr_index, dp)
    dp[curr_index][prev_index + 1] = max(include, exclude)
    return dp[curr_index][prev_index + 1]


# this is a better approach for converting the recursive code into dp (optimised)
def LIS_recursive_better(arr, curr_index, prev_index):
    # Base case
    if curr_index == len(arr):
        return 0
    exclude = LIS_recursive_better(arr, curr_index+1, prev_index)
    include = 0
    if (prev_index == -1 or arr[curr_index] > arr[prev_index]):
        include = 1 + LIS_recursive_better(arr, curr_index+1, curr_index)
    return max(include, exclude)
    

def LIS_recursive(arr, n, last_element):
    #Base case
    if n == 0:
        return 0
    
    curr_element = arr[n-1]
    if last_element > curr_element: # can take this in LIS
        return max(
            1 + LIS_recursive(arr, n-1, curr_element),
            LIS_recursive(arr, n-1, last_element)
        )
    else:
        return LIS_recursive(arr, n-1, last_element)


def get_dp_array(arr):
    n = len(arr)
    dp = [[None for _ in range(n+1)] for _ in range(n+1)]
    return dp


if __name__ == "__main__":
    a1 = [3, 10, 2, 1, 20]
    o1 = 3
    print(o1 == LIS_recursive(a1, len(a1), float('inf')))

    a2 = [30, 20, 10]
    o2 = 1
    print(o2 == LIS_recursive(a2, len(a2), float('inf')))

    a3 = [2, 2, 2]
    o3 = 1
    print(o3 == LIS_recursive(a3, len(a3), float('inf')))

    a4 = [10, 20, 35, 80]
    o4 = 4
    print(o4 == LIS_recursive(a4, len(a4), float('inf')))

    print(o1 == LIS_recursive_better(a1, 0, -1))
    print(o2 == LIS_recursive_better(a2, 0, -1))
    print(o3 == LIS_recursive_better(a3, 0, -1))
    print(o4 == LIS_recursive_better(a4, 0, -1))

    dp1 = get_dp_array(a1)
    dp2 = get_dp_array(a2)
    dp3 = get_dp_array(a3)
    dp4 = get_dp_array(a4)

    print("Memoised : ", o1 == LIS_memoised(a1, 0, -1, dp1))
    print("Memoised : ", o2 == LIS_memoised(a2, 0, -1, dp2))
    print("Memoised : ", o3 == LIS_memoised(a3, 0, -1, dp3))
    print("Memoised : ", o4 == LIS_memoised(a4, 0, -1, dp4))

    # print("Iterative : ", o1 == LIS(a1))
    # print("Iterative : ", o2 == LIS(a2))
    # print("Iterative : ", o3 == LIS(a3))
    # print("Iterative : ", o4 == LIS(a4))