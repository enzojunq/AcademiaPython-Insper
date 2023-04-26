def melhor_valor(partes: list, inventario: list[dict]) -> float:
    total = 0
    inventario_sorted = sorted(inventario, key=lambda x: x['valor'])

    for i in partes:
        for j in inventario_sorted:
            if i in j['equivalente']:
                total += j['valor']
                break
            elif i == j['serial']:
                total += j['valor']
                break

    return total


partes = ['X1D', 'A3B']

inventario = [
    {'serial': 'A3B', 'valor': 198.7, 'equivalente': []},
    {'serial': 'XP2', 'valor': 190.9, 'equivalente': ['Z3Z', 'A3B']},
    {'serial': 'XP1', 'valor':   5.1, 'equivalente': ['TH5', 'TH6', 'X3D', 'X1D']}
]

print(melhor_valor(partes, inventario))