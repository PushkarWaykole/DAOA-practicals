def isSafe(mat,row,col):
    
    
    #checking if the another queen is above 
    
    for i in range(row):
        if(mat[i][col]=='Q'):
            return False
        i=i+1
    
    #check for upper left diagonal
    (i,j)=(row,col)
    while(i>=0 and j>=0):
        if(mat[i][j]=='Q'):
            return False
        i=i-1
        j=j-1
        
    #check for upper right diagonal
    
    (i,j)=(row,col)
    while(i>=0 and j<len(mat)):
        if(mat[i][j]=='Q'):
            return False
        i=i-1
        j=j+1
        
    #if all checks are done and the quuen is safe to place 
    return True


def printMat(mat):
    for row in mat:
        print(str(row).replace(',',' ').replace('.','-').replace("'",""))
    print("\n")

def solve(mat,row):
    if(row==len(mat)):
        printMat(mat)
        return
        
    for col in range(len(mat)):
        if(isSafe(mat,row,col)):
            mat[row][col]="Q"
            solve(mat,row+1)
            mat[row][col]='.'  #backtracking
            
            
if __name__=='__main__':
    n=int(input("Enter the size of chessboard: "))
    
    mat=[['.' for _ in range(n)] for _ in range(n)]
    print("The solution of ",n," x ",n," queens are: ")
    solve(mat,0)
    
