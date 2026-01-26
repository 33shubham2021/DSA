"""
Problem - https://www.scaler.com/academy/mentee-dashboard/class/75286/assignment/problems/4176?navref=cl_tt_lst_nm

"""

def solve(self, A):
    m = len(A)
    n = len(A[0])
    total_cells = m*n
    blocked_cells = 0
    start_i = -1
    start_j = -1
    end_i = -1
    end_j = -1
    for i in range(m):
        for j in range(n):
            if A[i][j] == -1:
                blocked_cells += 1
            elif A[i][j] == 1:
                start_i = i 
                start_j = j 
            elif A[i][j] == 2:
                end_i = i 
                end_j = j
    empty_cells = total_cells - blocked_cells - 2
    params = {"m" : m,
                "n" : n,
                "blocked_cells" : blocked_cells,
                "empty_cells" : empty_cells,
                "end_i" : end_i,
                "end_j" : end_j}

    return self.count_paths(A, start_i, start_j, params, 0)
        

def count_paths(self, arr, i, j, params, travelled_cells):
    m = params["m"]
    n = params["n"]
    end_i = params["end_i"]
    end_j = params["end_j"]
    if i == end_i and j == end_j:
        if travelled_cells == params["empty_cells"] + 1:
            return 1
        else:
            return 0

    if  i >= m or j >= n or i < 0 or j < 0:
        return 0
    # -1 = blocked, -2 = already visited
    if arr[i][j] == -1 or arr[i][j] == -2:
        return 0
    
    original_val = arr[i][j]
    arr[i][j] = -2
    total_paths = (
            self.count_paths(arr, i+1, j, params, travelled_cells+1) +
            self.count_paths(arr, i-1, j, params, travelled_cells+1) +
            self.count_paths(arr, i, j+1, params, travelled_cells+1) +
            self.count_paths(arr, i, j-1, params, travelled_cells+1)
    )
    arr[i][j] = original_val
    return total_paths 

if __name__ == "__main__":
    pass