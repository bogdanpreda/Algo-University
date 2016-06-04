def countingSort(x,m):
    n=len(x)
    f=[0]*(m+1)
    y=[0]*n
    
    for i in range(n):
        f[x[i]]=f[x[i]]+1

    for i in range(1,m+1):
        f[i]=f[i]+f[i-1]
        
    for i in range(n-1,-1,-1):
        y[f[x[i]]-1]=x[i]
        f[x[i]]=f[x[i]]+1

    for i in range(n):
        x[i]=y[i]

    return x
x=[1,5,1,3,2,2]

