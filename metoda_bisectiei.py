def f(x):
    return x*x-3

def bisectie(a,b,epsilon):
    s = a
    d = b

    m = (s+d)/2.0
    if f(m) == 0:
        return m
    elif f(m)*f(s)<0:
        d = m
    else:
        s = m

    while abs(d-s)>=epsilon:
        m = (s+d)/2.0
        if f(m) == 0:
            return m
        elif f(m)*f(s)<0:
            d = m
        else:
            s = m
    return (d+s)/2

def bisectie_r(a,b,epsilon):
    s = a
    d = b

    m = (s+d)/2.0
    if f(m) == 0 or abs(b-a)<epsilon:
        return m
    elif f(m)*f(s)<0:
        return bisectie_r(a,m,epsilon)
    else:
        return bisectie_r(m,d,epsilon)

