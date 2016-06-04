a = [3,5,6,2,1,9,2]
c = 10

def impachetare(c,a):
    n = len(a)
    s = [0]*n
    for i in range(n):
        j = 0
        while s[j]+a[i]>c:
            j = j+1
        s[j] = s[j]+a[i]
    k = 0
    while s[k] != 0:
        k = k+1
    return k,s
