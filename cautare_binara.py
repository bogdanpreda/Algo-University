def cautare_binara(a,s,d,e):
    if d<s:
        return False
    else:
        m = int((s+d)/2)
        if e == a[m]:
            return True
        elif e < a[m]:
            return cautare_binara(a,s,m-1,e)
        else:
            return cautare_binara(a,m+1,d,e)

a = [9,10,11,12,13,19]
print cautare_binara(a,0,len(a)-1,19)
