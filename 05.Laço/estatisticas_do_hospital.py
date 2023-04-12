idade=float(input())
cont=0
crianca=0
adolescente=0
adulto25=0
adulto35=0
adulto59=0
idoso=0
while idade >= 0:
    if idade <= 11:
        crianca+=1
    elif idade <= 17:
        adolescente+=1
    elif idade <= 25:
        adulto25+=1
    elif idade <= 35:
        adulto35+=1
    elif idade <= 59:
        adulto59+=1
    else:
        idoso+=1
    cont+=1
    idade=int(input())

print(f"0-11 anos: {crianca*100/cont:.2f} %")
print(f"12-17 anos: {adolescente*100/cont:.2f} %")
print(f"18-25 anos: {adulto25*100/cont:.2f} %")
print(f"26-35 anos: {adulto35*100/cont:.2f} %")
print(f"36-59 anos: {adulto59*100/cont:.2f} %")
print(f"Acima de 60 anos: {idoso*100/cont:.2f} %")