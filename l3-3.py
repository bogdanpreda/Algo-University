lista = ["ana","casa","masa","calculator","informatica"]
lista2 = []
lista_vocale = []
for i in range(0,len(lista)):
    if len(lista[i]) < 5:
        lista2.append(lista[i])
        
    if lista[i][0] in ['a','e','i','o','u']:
        lista_vocale.append(lista[i])
        
print lista2
print lista_vocale
