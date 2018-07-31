def MaxGold(A,n,m):
    gold=[[0]*m for i in range(n)]

    for j in range(m-1,-1,-1):
        for i in range(n):
            x,y=i-1,j+1
            op1,op2,op3=0,0,0
            if(x<=n-1 and x>=0 and y>=0 and y<=m-1):
                op1=gold[x][y]
            x,y=i,j+1
            if(x<=n-1 and x>=0 and y>=0 and y<=m-1):
                op2=gold[x][y]
            x,y=i+1,j+1
            if(x<=n-1 and x>=0 and y>=0 and y<=m-1):
                op3=gold[x][y]
            
            gold[i][j]=(A[i][j] + max(op1,op2,op3))
    
    return max(gold[0:n])[0]
            

A=[[10,33,13,15],[22,21,4,1],[5,0,2,3],[0,6,14,2]]
n=len(A)
m=len(A[0])
print(MaxGold(A,n,m))