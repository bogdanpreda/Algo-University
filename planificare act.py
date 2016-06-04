n = 4
t = [2,3,4,2]
p = [4,3,2,1]
def sortare(x,x2):
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

def planificare(p,t):
    n = len(p)
    sortare(p,t)
    profit = 0
    s = [0]*(n+1)
    for i in range(n):
        poz = t[i]
        while s[poz]>0 and poz>1:
            poz = poz-1
        if s[poz] == 0:
            s[poz] = i+1
            profit = profit+p[i]
            print "se planifica activitatea",i+1,"la pozitia",poz
        else:
            print "actvitatea,",i+1,"nu se poate planifica"
    return profit,s
