c = 40
k = [1,3,1,2,5]
v = [25,20,10,5,1]
def selectie(x,x2):
    n = len(x)
    for i in range(n-1):
        k = i
        for j in range(i+1,n):
            if x[k]<x[j]:
                k = j
        if k!=i:
            aux = x[k]
            x[k]=x[i]
            x[i]=aux

            aux = x2[k]
            x2[k]=x2[i]
            x2[i]=aux
def greedy(c,v,k):
    n = len(v)
    selectie(v,k)
    s = [0]*n
    i = 0
    while c>0 and i<=n:
        aux = c/v[i]
        if aux<=k[i]:
            s[i] = aux
            c = c%v[i]
        else:
            s[i] = k[i]
            c = c - s[i]*k[i]
        i = i+1
    return c, s
