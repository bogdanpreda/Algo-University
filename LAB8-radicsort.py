def countingSort2(x,m,c):
    n=len(x)
    f=[0]*(m+1)
    y=[0]*n
    p=10**c
    for i in range(n):
        j=(x[i]/p)%10
        f[j]=f[j]+1

    for i in range(1,m+1):
        f[i]=f[i]+f[i-1]
        
    for i in range(n-1,-1,-1):
        j=(x[i]/p)%10
        y[f[j]-1]=x[i]
        f[j]=f[j]-1

    for i in range(n):
        x[i]=y[i]
    return x

x=[1256,138,11,725]

def radixSort(x,k):
    #k=nr maxim de cifre
    for i in range(0,k+1):
        x=countingSort2(x,9,i)

    return x
