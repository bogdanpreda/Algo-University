import random
p = []
for i in range(1,366):
    p.append(int(random.random()*61))

s = 0
for i in p:
    if p[i] == 0:
        s = s+1
print "numarul de zile fara precipitatii este",s

lunile_anului = [31,28,31,30,31,30,31,31,30,31,30,31,30,31]
sum = 0
nr = 0
j = 1
for i in p:
    sum = sum+p[i]
    if j == lunile_anului[nr]:
        print "media precipitatiilor lunii",nr+1,"este:", sum*1.0/lunile_anului[nr]
        nr = nr+1
        sum = 0
        j = 0
    j = j+1
    
sum = 0
for i in p:
    sum = sum+p[i]
print "media anuala a precipitatiilor este", sum*1.0/365
