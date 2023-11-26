# N queens && Constraint satisfaction problem


def is_safe(board,row,col,n):

    for i in range(row):
        if board[i][col]=='Q':
            return False
        
    for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j]=='Q':
            return False
        
    for i, j in zip(range(row,-1,-1), range(col,n)):
        if board[i][j]=='Q':
            return False
        
    return True
       


def solve(board,row,n):
    if row==n:
        for i in range(n):
            for j in range(n):
                print (board[i][j],end=" ")
            print()
        return True
    
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]='Q'
            if solve(board,row+1,n):
                return True
            board[row][col]=0

    return False

def solve_n_queen(n):
    board=[[0]*n for _ in range(n)]

    solve(board,0,n)

n=int(input("Enter number of queens : "))
if(n==2 or n==3):
    print("No solution exists : ")
else:
    solve_n_queen(n)
