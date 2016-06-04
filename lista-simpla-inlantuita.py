
class Nod:
    
    def __init__(self,info,urmat):
        self.info = info
        self.urmat = urmat
        
    def __repr__(self):
        return str(self.info)
        
class ListaSimpluInlantuita:
    
    def __init__(self):
        self.inceput = None
        
    def adaugareFata(self,x):
        if self.inceput == None:
            self.inceput = Nod(x,None)
        else:
            nouNod = Nod(x,self.inceput)
            self.inceput = nouNod
    
    def adaugareSpate(self,x):
        if self.inceput == None:
            self.inceput = Nod(x,None)
        else:
            aux = self.inceput
            while aux.urmat != None:
                aux = aux.urmat
            nouNod = Nod(x,None)
            aux.urmat = nodNou

    def stergeFata(self):
        if self.inceput != None:
            self.inceput = self.inceput.urmat
        else:
            print "lista este vida"

    def stergeSpate(self):
        if self.inceput.urmat == None:
            self.inceput = None
        else:
            aux = self.inceput
            while aux.urmat.urmat != None:
                aux = aux.urmat
            aux.urmat = None

    def cautareEl(self,x):
        aux = inceput
        while aux != None and aux.info !=x:
            aux = aux.urmat
        return aux

    def cautareIndex(self,k):
        i = 0
        aux = self.inceput
        while aux != None and i<k:
            aux = aux.urmat
            i += 1
        return aux

    def adaugaIntre(self,x,y):
        if aux!=None:
            aux = self.cautare(x)
            nodNou = Nod(y,aux.urmat)
            aux.urmat = nodNou
    
    def __repr__(self):
        r = "["
        aux = self.inceput
        while aux != None:
            r += str(aux)+", "
            aux = aux.urmat
        if self.inceput != None:
            r = r[:len(r)-2]
        r+="]"
        
        return r
def reuniune(l,r):
    aux = l.inceput
    while aux !=None:
        if not r.cautareEl(aux.info):
            r.adaugareFata(aux.info)
        aux = aux.urmat
    return r
l=ListaSimpluInlantuita()

