"""
Docstring for dynamic_programming.0_1_knapsack.brute_force_print_all
1. print_all_combinations - this is not possible probably, becuase we want answers of 
    smaller problem to calculate the current combination.
2. get_all_combination
3. having solved the combination problem brute force way, look for similar questions on chatgpt
"""
def get_all_combinations(arr , currIndex):
    #Base case
    l = len(arr)
    #If only one element present, its just pick or not pick (empty)
    if (currIndex == l-1):
        return [arr[currIndex] , ""]
    
    #get all the smaller combinations first
    r = get_all_combinations(arr , currIndex+1)
    ans = []
    for i in range(0,len(r)):
        ans.append(arr[currIndex] + r[i]) #pick current-indexed element
        ans.append(r[i])                  #not pick current-indexed element
    return ans



def main():
    arr = ["a", "b", "c", "d"]
    out = get_all_combinations(arr,0)
    print("Total number of combinations are :",len(out))
    for i in out:
        if (len(i) == 0):
            print("Empty String")
        print(i)

if __name__ == "__main__":
    main()