def contabiliza_combustivel(dict):
 
    new_dict = {}

    for dia, dados in dict.items():
        tipo_combustivel = dados['tipo']
        litros = dados['litros']
        custo = dados['custo']

        if tipo_combustivel not in new_dict:
            new_dict[tipo_combustivel] = {
                'total litros': litros,
                'custo por litro': custo
            }
        else:
            new_dict[tipo_combustivel]['total litros'] += litros
            new_dict[tipo_combustivel]['custo por litro'] += custo

    for combustivel,valor in new_dict.items():
        new_dict[combustivel]['custo por litro']=valor['custo por litro']/valor['total litros']

    
    return new_dict


dict={
    'dia 1': {
        'tipo': 'Etanol',
        'litros': 20,
        'custo': 50.0
    },
    'dia 4': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 150.5
    },
    'dia 10': {
        'tipo': 'Gasolina',
        'litros': 15,
        'custo': 49.5
    },
    'dia 14': {
        'tipo': 'Etanol',
        'litros': 30,
        'custo': 70.0
    }
}
print(contabiliza_combustivel(dict))

'''
RETURN
{
    'Etanol': {
        'total litros': 50,
        'custo por litro': 2.4
    },
    'Gasolina': {
        'total litros': 40,
        'custo por litro': 5
    }
}
'''