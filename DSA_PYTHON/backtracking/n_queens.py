"""
Problem - https://www.scaler.com/academy/mentee-dashboard/class/75306/assignment/problems/141?navref=cl_tt_lst_nm
and -     https://leetcode.com/problems/n-queens/description/

1. for N*N chessboard, find weather we can place N queens on the board (return true or false)
2. return the solution boards as an array of 2d arrays (this is required in above problem)
    https://www.geeksforgeeks.org/dsa/n-queen-problem-backtracking-3/ -> this as well
3. return the total count of solutions 

"""
# this is my solution of the boolean N-Queens problem
def place_queen(N, occupied, placed, start_row=0):
    # N = board size , placed = number of queens placed till now 
    if N == 0:
        return False
    if placed == N: # all queens are placed
        return True
    
    # try placing 1 queen at all positions one by one
    for i in range(start_row, N):
        for j in range(N):
            if occupied[i][j] == 0:
                mark_occupied_cells(occupied, i, j, 1)
                if place_queen(N, occupied, placed+1, i+1):
                    return True
                mark_occupied_cells(occupied, i, j, -1)
    return False

def mark_occupied_cells(occupied, i, j, value):
    N = len(occupied)
    # Mark row and column
    for t in range(N):
        occupied[i][t] += value  # Mark whole row
        occupied[t][j] += value  # Mark whole column
        
    # Mark diagonals
    # Note: We subtract 'value' once from the intersection (i,j) 
    # because it was added twice above (once for row, once for col)
    occupied[i][j] -= value
    
    diff_constant = i - j
    sum_constant = i + j
    
    for r in range(N):
        for c in range(N):
            # Skip the queen's own position to avoid double counting
            if r == i and c == j:
                continue
                
            if (r - c == diff_constant) or (r + c == sum_constant):
                occupied[r][c] += value


if __name__ == "__main__":
    ans = [False, True, False, False, True, True, True, True, True, True, True]
    for N in range(11):
        visited = [[0 for _ in range(N)] for _ in range(N)]
        print("Match value = ",ans[N] == place_queen(N, visited, 0))




"""
1	True	1
2	False	0
3	False	0
4	True	2
5	True	10
6	True	4
7	True	40
8	True	92
9	True	352
10	True	724
"""