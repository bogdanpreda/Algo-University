
def selectie(x):
    nc = 0
    nm = 0
    n = len(x)
    for i in range(n-1):
        k = i
        for j in range(i+1,n):
            nc = nc+1
            if x[k]>x[j]:
                k = j
        nc = nc+1
        if k!=i:
            aux = x[k]
            x[k]=x[i]
            x[i]=aux
            nm = nm+3
    return x,nc,nm
    
x=[3, 6, 2, 1, 5]
print selectie(x)
