def calcula_dano(heroi):
    forca = heroi['força']
    equipamentos = heroi['equipamentos']
    dano=forca
    if not equipamentos == {}:
        for equipamento in equipamentos:
            dano+=equipamento['força']
        return dano

    else:
        return dano



dict = {
    'nome': 'Herói',
    'força': 4,
    'vida': 25,
    'equipamentos': [
        {
            'nome': 'Martelo Mortal',
            'força': 15, 
        },
        {
            'nome': 'Luva Leve',
            'força': 2, 
        },
    ],
}
print(calcula_dano(dict))