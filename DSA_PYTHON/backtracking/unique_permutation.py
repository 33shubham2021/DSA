"""
Docstring for greedy.unique_permutation
Problem - https://www.scaler.com/academy/mentee-dashboard/class/75286/assignment/problems/134?navref=cl_tt_lst_nm
"""
def get_permutation(arr, f, idx, temp, ans):
    n = len(arr)
    if idx == n:
        ans.append(temp[:])
        return
    for i in range(len(f)):
        if f[i] != 0:
            f[i] -= 1
            temp[idx] = i
            get_permutation(arr, f, idx+1, temp, ans)
            f[i] += 1
    

def get_frequency_array(arr):
    f = [0] * 10
    for i in range(len(arr)):
        f[arr[i]] += 1
    return f

if __name__ == "__main__":
    arr = [10, 9, 10, 9, 10]
    freq_array = get_frequency_array(arr)
    ans = []
    temp = [None] * len(arr)
    get_permutation(arr, freq_array, 0, temp, ans)
    print(ans)
