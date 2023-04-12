precos=[]
i=0
maior=0
menor=9999
indice_maior=0
indice_menor=0
numero_de_precos=float(input())
while i < numero_de_precos:
    preco=float(input())
    if preco<menor:
        menor=preco
        indice_menor=i+1
    if preco>maior:
        maior=preco
        indice_maior=i+1
    precos.append(preco)
    i+=1
media=sum(precos)/len(precos)

print(f'O dia {indice_menor} foi o melhor dia para compra')
print(f'O dia {indice_maior} foi o pior dia para compra')
print(f'O preço médio cobrado foi de {media:.2f}')