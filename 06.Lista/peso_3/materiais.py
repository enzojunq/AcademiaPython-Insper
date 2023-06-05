def precisa_repor(materiais_dict, salas):
    responsavel = {}
    if materiais_dict == {} or salas == {}:
        return responsavel
    for sala, info in salas.items():
        materiais_sala = info['materiais']
        for material, valor in materiais_sala.items():
            if material not in materiais_dict:
                continue
            if valor < materiais_dict[material]['nivel minimo']:
                if materiais_dict[material]['responsavel'] not in responsavel:
                    responsavel[materiais_dict[material]['responsavel']] = [{'sala': sala, 'material': material}]
                else:
                    responsavel[materiais_dict[material]['responsavel']].append({'sala': sala, 'material': material})
    return responsavel


materiais_dict={'folha a4': {'nivel minimo': 125, 'responsavel': 'maria'}, 'fio dental': {'nivel minimo': 3.6, 'responsavel': 'pedro'}, 'cafe': {'nivel minimo': 20, 'responsavel': 'maria'}}
salas={'banheiro terreo 1': {'metragem': 15.8, 'volts': [110, 220], 'materiais': {'sabonete': 3.3, 'fio dental': 2.5, 'celulares': 4}}, 'recepcao predio 1': {'metragem': 27.3, 'volts': [110], 'materiais': {'computadores': 2}}}
print(precisa_repor(materiais_dict,salas))