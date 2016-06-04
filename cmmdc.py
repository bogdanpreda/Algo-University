def cmmdc(a,b):
    if a==b:
        return a
    elif a>b:
        return cmmdc(a-b,b)
    else:
        return cmmdc(a,b-a)
