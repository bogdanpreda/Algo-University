a = [1,1,2,2,3,4,6,7,7,9]

def eliminare(a):
    k = 0
    n = len(a)
    for i in range(n-1):
        if a[i] < a[i+1]:
            k = k+1
            a[k] = a[i+1]
    return a

def cautare(a,e):
    i = 0
    n = len(a)
    gasit = False
    while i<len(a) and gasit == False:
        if a[i] == e:
            gasit = True
        else:
            i = i+1

    return gasit

def intersectie(a,b):
    c = []
    m = len(b)
    for i in range(m):
        if cautare(a,b[i]):
            c.append(b[i])

    return c

def reuniune(a,b):
    c = a
    for i in b:
        if not cautare(a,i):
            c.append(i)

    return c
