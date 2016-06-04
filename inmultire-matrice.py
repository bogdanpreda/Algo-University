def prod(a,x):
    
    m=len(a)
    n=len(a[0])
    y=[[0]*m]
    for i in range(0,m):
        y[i]=0
        for j in range(0,n):
            y[i]= y[i]+a[i][j]*x[j]

    print y

            
a=[[1,2,3],[4,5,4]]
x=[[2],[2],[2]]
