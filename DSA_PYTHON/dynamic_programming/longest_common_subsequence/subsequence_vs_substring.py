"""
Docstring for dynamic_programming.longest_common_subsequence.subsequence_vs_substring
TODO - print the subsequence/substring in particular order
"""
def get_all_subarray(s):
    #Base
    if (len(s) == 0):
        return []
    r = get_all_subarray(s[1:])
    ans = []
    ans.append(s[0:1])
    for i in range(len(r)):
        ans.append(r[i])
        first_char = r[i][0:1]
        if first_char == s[1:2]:
            ans.append(s[0:1] + r[i])
    return ans

def get_all_subsequence(s):
    #Base
    if len(s) == 0:
        return []
    r = get_all_subsequence(s[1:])
    ans = []
    ans.append(s[0:1])
    for i in range(len(r)):
        ans.append(r[i])
        ans.append(s[0:1] + r[i])
    return ans

def LCS_brute_force(s1, s2):
    a1 = get_all_subsequence(s1)
    a2 = get_all_subsequence(s2)
    max_length = 0
    for str1 in a1:
        if str1 in a2 and len(str1) > max_length:
            max_length = len(str1)
    return max_length


if __name__ == "__main__":
    s = "abc"
    subsequences = get_all_subsequence(s)
    print("Printing subsequences")
    for i in subsequences:
        print(i)
    
    subarrays = get_all_subarray(s)
    print("Printing subarrays")
    for i in subarrays:
        print(i)

    #LCS Code
    print("####  LCS  ####")
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print(LCS_brute_force(s1 , s2))