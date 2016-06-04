def mergesort(x,s,d,nc):
    if s<d:
        m = (s+d)/2
        x,nc = mergesort(x,s,m,nc)
        x,nc = mergesort(x,m+1,d,nc)
        x,nc = interclasare(x,s,m,d,nc)
    return x,nc
def interclasare(x,s,m,d,nc):
    i = s
    j = m+1
    k = 0
    c = []
    while i<=m and j<=d:
        if x[i]<x[j]:
          c.append(x[i])
          nc = nc+1
          i = i+1
        else:
            c.append(x[j])
            nc = nc+1
            j = j+1
    while i<=m:
        c.append(x[i])
        nc = nc+1
        i = i+1
    while j<=d:
        c.append(x[j])
        nc = nc+1
        j = j+1
    for i in range(0,len(c)):
        x[i+s] = c[i]
    return x,nc

x = [5,3,2,5,23,534,1,6]

x = [234,125,52,32,3,5]
