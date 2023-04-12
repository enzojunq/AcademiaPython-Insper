
cont=0
maior=0
numero=0

for i in range(2,999):

    if cont>=maior:
        maior=cont
        numero=i 
        
    while i!=1:
        if i%2==0:
            i=i/2
            cont+=1    
        else:
            i=i*3+1
            cont+=1
    
    

    cont=0
print(numero)
            