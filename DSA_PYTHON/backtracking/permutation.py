"""
Docstring for greedy.permutation
Problem - https://www.scaler.com/academy/mentee-dashboard/class/75286/assignment/problems/138/submissions
"""
import itertools

def print_permutation(arr, visited, idx, ans):
    n = len(arr)
    if idx == n:                                         # reached the end, so print the combination
        print(ans)
        return
    for i in range(n):
        if (not visited[i]):
            visited[i] = True                            # DO step
            ans[idx] = arr[i]                            # fixing the char at index=idx
            print_permutation(arr, visited, idx+1, ans)  # move forward
            visited[i] = False                           # UNDO step

def print_permutation_sorted(arr, visited, idx, ans):
    sorted(arr)
    print_permutation(arr, visited, idx, ans)

if __name__ == "__main__":
    arr = ['a', 'b', 'c']
    visited = [False] * len(arr)
    ans = [None] * len(arr)
    print_permutation(arr, visited, 0, ans)

    # print in sorted order
    print("########    Sorted Order    ########")
    arr1 = ['d', 'x', 'f', 'p']
    visited1 = [False] * len(arr1)
    ans1 = [None] * len(arr1)
    print_permutation_sorted(arr1, visited1, 0, ans1)

    # generating permutation using python library methods
    print("########    Library Methods    ########")
    # Get all permutations of length 3 (default)
    #data = [1, 2, 3]
    perms = itertools.permutations(arr)

    # It returns an iterator, so we convert to a list to see the results
    print(list(perms))
    


