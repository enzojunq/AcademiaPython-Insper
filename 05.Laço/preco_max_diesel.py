
dias = int(input())
soma=0

for i in range(1,dias+1):
    preco=float(input())
    soma+=preco
media=soma/dias
print(f'O preço médio cobrado foi de {media:.2f}')