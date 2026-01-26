"""
Problem - https://www.scaler.com/academy/mentee-dashboard/class/75286/assignment/problems/148/chatgpt-help
TODO - debug and fix this code, the output sequence is not equal to what is expected in the question,
       although, all the subsets are getting generated
"""

def subsets(arr, idx, temp, answer):
    # Base Case: When we've made a decision for every element
    if idx == len(arr):
        answer.append(temp[:])
        return
    
    # Choice 1: NOT TAKE the element at arr[idx]
    subsets(arr, idx + 1, temp, answer)
    
    # Choice 2: TAKE the element at arr[idx]
    temp.append(arr[idx])
    subsets(arr, idx + 1, temp, answer)
    
    # Backtrack: Remove the element to keep 'temp' clean for other branches
    temp.pop()

if __name__ == "__main__":
    arr = [1, 2, 3]
    n = len(arr)
    temp = []
    answer = []
    subsets(arr, 0, temp, answer)
    print(answer)