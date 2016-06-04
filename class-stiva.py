class Stiva:
    
    def __init__(self,nmax):
        self.nmax = nmax
        self.data = [None]*nmax
        self.v = 0
    
    def isPlin(self):
        return self.v == self.nmax

    def isGoala(self):
        return self.v == 0

    def push(self,e):
        if self.isPlin():
            print "stiva plina- nu se mai pot adauga elemente"
        else:
            self.data[self.v] = e
            self.v += 1
    def pop(self):
        if self.isGoala():
            print "Stiva este goala - nu se pot scoate elemente"
        else:
            self.v = self.v-1
            return self.data[self.v]

    def __repr__(self):
        r="Stiva:"
        for i in range(self.v):
            r+=str(self.data[i])+" "
        r+="Reprezentare interna "+str(self.data)
        return r

def reverse(cuv):
    s = Stiva(len(cuv))
    for i in range(len(cuv)):
        s.push(cuv[i])

    while(not s.isGoala()):
        print s.pop(),

html=["<html>","<body>","</body>","</html>"]

def verificare(html):
    s = Stiva(len(html))
    for i in range(len(html)):
        tc = html[i]
        if tc[1]!='/':
            s.push(tc)
        else:
            el = s.pop()
            if el[1:] != tc[2:]:
                return False
    return s.isGoala()
    
    
