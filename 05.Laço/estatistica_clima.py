dias=int(input("Digite a quantidade de dias: "))
dias_chuvas=0
dias_frio=0
dias_guarda_chuva=0
dias_casaco=0
for i in range(dias):
    choveu=input("Choveu? (s/n): ")
    if choveu=="S":
        dias_chuvas+=1

    temp_min=float(input("Digite a temperatura mínima: "))
    if temp_min<20:
        dias_frio+=1

    guarda_chuva=input("tinha guarda-chuva? (s/n): ")
    if guarda_chuva=="S" and choveu=="S":
        dias_guarda_chuva+=1

    casaco=input("tinha casaco? (s/n): ")
    if casaco=="S" and temp_min<20:
        dias_casaco+=1

print(f'Choveu em {dias_chuvas} de {dias} dias')
print(f'Fez frio em {dias_frio} de {dias} dias')
print(f'Usou guarda-chuva em {dias_guarda_chuva} de {dias_chuvas} dias de chuva')
print(f'Usou casaco em {dias_casaco} de {dias_frio} dias de frio')

