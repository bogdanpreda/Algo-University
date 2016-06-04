x = [6,3,2,5,1]

def insertie(x):
    nc = 0
    nm = 0
    n = len(x)
    for i in range(1,n):
        aux = x[i]
        nm = nm+1
        j = i-1
        while j>=0 and aux<x[j]:
            nc = nc+1
            x[j+1] = x[j]
            j = j-1
            nm = nm+1

        nc = nc+1
        x[j+1] = aux
        nm = nm+1

    return x, nc, nm

