def ShockerSort(x):
    n=len(x)
    s=0
    d=n
    t=0
    for i in range(s,d):
        if x[i]>x[i+1]:
            aux = x[i]
            x[i] = x[i+1]
            x[i+1] = aux
            t=i
    if t!=0:
        d=t
        t=0
        for i in range (d,s+1,-1):
            if x[i]<x[i+1]:
                aux = x[i]
                x[i] = x[i+1]
                x[i+1] = aux
                t=i
        s=t
    while t!=0 and s<d:
        t=0
        for i in range(s,d,-1):
            if x[i]>x[i+1]:
                aux = x[i]
                x[i] = x[i+1]
                x[i+1] = aux
                t=i
        if t!=0:
            d=t
            t=0
            for i in range (d,s+2,p1):
                if x[i]<x[i+1]:
                    aux = x[i]
                    x[i] = x[i+1]
                    x[i+1] = aux
                    t=i
            s=t
    return x
x=[1,9,5,3,2]
        
