class Coada:
    def __init__(self, nmax):
        self.nmax = nmax
        self.s = -1
        self.f = 0
        self.data = [None]*(nmax+1)

    def isGoala(self):
        return self.f == self.avIndex(self.s)

    def isPlina(self):
        return self.f == self.avIndex(self.avIndex(self.s))

    def add(self, e):
        if self.isPlina():
            print "Coada plina"
            return
        self.s = self.avIndex(self.s)
        self.data[self.s] = e

    def eliminare(self):
        if self.isGoala():
            print "coada goala"
            return
        val = self.data[self.f]
        self.f = self.avIndex(self.f)
        return val

    def avIndex(self,p):
        if p==self.nmax:
            return 0
        else:
            return p+1

    def __repr__(self):
        r = "coada: "
        p = self.f
        while(self.f!=avIndex(s)):
            r+= self.data[p]
            p = self.avIndex(p)
        r+="Reprezentare interna"+str(self.data)
        return r

    def numaratorare(n,m):
        c = Coada(n)
        for i in range(n):
            c.add(i+1)
        for i in range(n-1):
            c.add(c.elimina())
        c.elimina()
        print "nuamr ramas"+c.elimina()
