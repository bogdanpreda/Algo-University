def identific(p):
    m = p[1]
    im = 1
    for i in range(2,len(p)):
        if p[i]>m:
            m = p[i]
            im = i
    return im

def inversare(i,p):
    k = i
    h = len(p)-1
    while k<h:
        aux = p[k]
        p[k] = p[h]
        p[h] = aux
        k = k+1
        h = h-1
    return p

def mini(i,p):
    k2 = 0
    k = i
    for i in range(i,len(p)-1):
        k = i+1
        if p[k]>p[i-1]:
            k2 = k
            break
    return k2

def perm(n):
    p = []
    for i in range(n):
        p.append(i)
    print p
    i = identific(p)
    while i>0:
        k = minim(p,i)
    
    
