idades = []
while True:
    idade = float(input())
    if idade < 0:
        break
    idades.append(idade)

total_pacientes = len(idades)
faixas_etarias = {
    "0-11 anos": 0,
    "12-17 anos": 0,
    "18-25 anos": 0,
    "26-35 anos": 0,
    "36-59 anos": 0,
    "Acima de 60 anos": 0,
}

for idade in idades:
    if idade <= 11:
        faixas_etarias["0-11 anos"] += 1
    elif idade <= 17:
        faixas_etarias["12-17 anos"] += 1
    elif idade <= 25:
        faixas_etarias["18-25 anos"] += 1
    elif idade <= 35:
        faixas_etarias["26-35 anos"] += 1
    elif idade <= 59:
        faixas_etarias["36-59 anos"] += 1
    else:
        faixas_etarias["Acima de 60 anos"] += 1

for faixa_etaria, num_pacientes in faixas_etarias.items():
    percentual = num_pacientes / total_pacientes * 100
    print(f"{faixa_etaria}: {percentual:.2f} %")
