def quicksort(x,s,d,nc):
    if s<d:
        nc,q = partitionare(x,s,d,nc)
        x,nc = quicksort(x,s,q,nc)
        x,nc = quicksort(x,q+1,d,nc)
    return x,nc

def partitionare(x,s,d,nc):
    v = x[s]
    i = s-1
    j = d+1
    while i<j:
        i = i+1
        nc = nc+1
        while x[i]<v:
            i = i+1
            nc = nc+1
        j = j-1
        nc = nc+1
        while x[j]>v:
            j = j-1
            nc = nc+1
        if i<j:
            aux  = x[i]
            x[i] = x[j]
            x[j] = aux

    return nc,j
x = [5,3,2,5,23,534,1]

x = [234,125,52,32,3,5]
