"""
Problem - https://www.geeksforgeeks.org/problems/candy/1
"""
def minCandy(arr):
        # Code here
        l = len(arr)
        c = [1 for _ in range(l)]
        #moving left to right
        for i in range(1,l):
            if (arr[i] > arr[i-1]):
                c[i] = 1 + c[i-1]
        
        #moving right to left
        for i in range(l-2 , -1, -1):
            if (arr[i] > arr[i+1]):
                c[i] = max(c[i+1]+1 , c[i])
        return sum(c)


