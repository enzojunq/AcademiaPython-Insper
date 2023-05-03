def separa_trios(nomes:list):
    trios = []
    for i in range(0, len(nomes), 3):
        trios.append(nomes[i:i+3])
    return trios

print(separa_trios(['Ana', 'Bia', 'Celi', 'Dora', 'Eva', 'Fabi', 'Gabi', 'Iara', 'Jana']))