"""
In this question, you are given a grid (or matrix) with M rows and N columns. 
Each cell in the grid contains either a 0 or a 1. 
Your task is to find any cell that contains a 0 and change all the cells in its row and column to 0. The tricky part is that you have to do this without using any extra space, like another grid or a list.
 input: 
 3 4 
 1 1 0 0 
 0 1 1 1 
 1 0 1 0 
 output:

0 0 0 0
0 0 0 0
0 0 0 0

"""
def zero(matrix,m,n):
    col0=1
    
    for i in range(m):
        if matrix[i][0]==0:
            col0=0 
        for j in range(1,n):
            if matrix[i][j]==0:
                matrix[i][0]=0 
                matrix[0][j]=0 
                
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0 
                
    if matrix[0][0]==0:
        for i in range(n):
            matrix[0][i]=0 
    if col0==0:
        for i in range(m):
            matrix[i][0]=0
            
    return matrix





m,n=list(map(int, input().split()))
matrix=[]

for i in range(m):
    a=list(map(int, input().split()))
    matrix.append(a)


    
result=zero(matrix,m,n)
for i in result:
    print(*i)