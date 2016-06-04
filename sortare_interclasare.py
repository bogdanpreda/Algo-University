x = [6,3,2,5,1]

def interschimbare(x):
    nc = 0
    nm = 0
    n = len(x)
    m = n

    t = 0
    for i in range(m-1):
        nc = nc+1
        
        if x[i]>x[i+1]:
            aux    = x[i]
            x[i]   = x[i+1]
            x[i+1] = aux;

            t=i
            nm = nm+1
    m = t+1
    while t>0:
        t = 0
        for i in range(m):
            nc = nc+1
            
            if x[i]>x[i+1]:
                aux    = x[i]
                x[i]   = x[i+1]
                x[i+1] = aux;

                t=i
                nm = nm+1
        m = t+1
    return x,nc,nm
