a=[5,10,1,3,5,9]
for i in range(len(a)-1,0,-1):
    if(a[i]<a[i-1]):
       aux = a[i]
       a[i]=a[i-1]
       a[i-1]=aux

print a
       
    
