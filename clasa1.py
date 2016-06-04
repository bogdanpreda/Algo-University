class Bicicleta:
    
    def __init__(self,producator,pret):
        self.producator = producator
        self.pret =pret

    def modificaPret(self,val):
        self.pret = val

    def __repr__(self):
        return "Bicicleta: "+str(self.producator)+" "+str(self.pret)

b = Bicicleta("Cube","3000 lei")
print b


                               
                               