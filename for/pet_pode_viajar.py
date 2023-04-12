def pet_pode_viajar(infos,limites,passagens):

    total_pets=0    # conta o total de pets em voo

    for passagem in passagens:
        if len(passagem[1])!=0:
            if 'pet_cabine' in passagem[1]:
                total_pets+=1
    if total_pets>=limites[0]:
        return False
    elif infos[2]+infos[3]>limites[1]:
        return False
    elif infos[4][0]>limites[2][0] or infos[4][1]>limites[2][1] or infos[4][2]>limites[2][2]:
        return False
    elif infos[5]!='S':
        return False
    else:
        return True
    


passagens=[
  ['1A', ['menor_desacompanhado']],
  ['5C', ['pet_cabine', 'alergia']],
  ['6D', []],
  ['7A', ['pet_cabine']],
  ['7A', ['cadeira_rodas']],
  ['9A', ['pet_cabine']],
  ['9B', []],
  ['9C', []]
]

limites=[4, 9.0, [25.0, 30.0, 45.0]]

infos=['Caipira', 'cachorro', 4.5, 1.0, [20.0, 30.0, 40.0], 'S']

print(pet_pode_viajar(infos,limites,passagens))